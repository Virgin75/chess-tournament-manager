import models
import views
import db
import re
import os


class Main_menu_controller:
    def __init__(self):
        self.view = views.Views()
        self.choices = {
            "1": self.create_tournament,
            "2": self.add_player,
            "3": self.edit_player,
            "4": self.start_round,
            "5": self.generate_reports,
            "6": self.import_data
        }
        self.players_created = 0
        self.player_instances = []
        self.tournament_created = 0
        self.tournament_instance = None
        self.current_round = 0
        self.round_instances = []

    def run(self):
        while True:
            if len(self.round_instances) == 4:
                '''When all the rounds have been played, a new tournament can be created'''
                self.players_created = 0
                self.player_instances = []
                self.tournament_created = 0
                self.tournament_instance = None
                self.current_round = 0
                self.round_instances = []
            go_to = self.view.main_menu_view(
                self.players_created, self.tournament_created, self.current_round,
                self.tournament_instance, db.database.name)
            action = self.choices.get(go_to)
            if action:
                action()
            else:
                views.Views().wrong_input_view(go_to)

    def create_tournament(self):
        view = views.Tournament_views()
        if self.tournament_created == 0:
            tournament_data = view.create_tournament_view()
            tc = Tournament_controller(tournament_data)
            if tc.is_data_valid():
                tournament = models.Tournament(*tournament_data)
                view.success_message_tournament(tournament.name)
                self.tournament_created += 1
                self.tournament_instance = tournament
                tournament.save_to_db()
        else:
            '''A tournament has already been created'''
            view.already_created_view()

    def add_player(self):
        if self.tournament_instance is None:
            return views.Views().error_step_view()
        view = views.Players_views()
        if self.players_created <= 7:
            player_data = view.create_player_view(self.players_created + 1)
            pc = Player_controller(player_data)
            if pc.is_data_valid():
                player = models.Player(*player_data)
                view.success_message_player(player.first_name, player.last_name)
                self.players_created += 1
                self.player_instances.append(player)
                player.save_to_db()
                self.tournament_instance.update_players_list(player)
        else:
            '''More than 8 player have already been created'''
            view.too_many_players_view()

    def edit_player(self):
        edit_player_controller = Edit_player_menu_controller(
            self.player_instances)
        edit_player_controller.run()

    def start_round(self):
        view = views.Rounds_views()
        # The round cannot start if one of the 3 conditions below is met
        if self.players_created < 8:
            return view.not_enough_players_view()
        if self.tournament_created == 0:
            return view.no_tournament_created_view()
        if self.current_round == 4:
            return view.no_more_round_view()

        round_name = view.start_round_view(self.current_round)
        my_round = models.Round(round_name, self.tournament_instance.id)
        self.round_instances.append(my_round)

        # Generate paires first round
        if self.current_round == 0:
            my_round.generer_paires_round1(self.player_instances)

        # Generate paires following rounds
        else:
            my_round.generer_paires_next_rounds(self.player_instances)

        match_list = my_round.match_instances
        view.display_matches_view(match_list)

        # Set the round results
        rc = Set_matches_results_menu_controller(match_list)
        rc.run()

        my_round.set_end_time()
        self.tournament_instance.update_rounds_list(my_round)
        self.current_round += 1

    def generate_reports(self):
        grmc = Generate_reports_menu_controller()
        grmc.run()

    def import_data(self):
        idmc = Import_data_menu_controller()
        players, tournaments, valid_json_file = idmc.run()

        if valid_json_file is False:
            return

        def get_player_inst_from_id(id):
            players_list = self.player_instances
            result = [player for player in players_list if player.id == id]
            return result[0]

        # Import basic tournament data
        self.tournament_created = len(tournaments)
        last_tournament = len(tournaments) - self.tournament_created
        self.tournament_instance = models.Tournament(
            tournaments[last_tournament]["name"],
            tournaments[last_tournament]["place"],
            tournaments[last_tournament]["start_date"],
            tournaments[last_tournament]["end_date"],
            tournaments[last_tournament]["description"],
            tournaments[last_tournament]["time_control"],
            id=tournaments[last_tournament]["id"])

        # Import players data
        self.players_created = len(players)
        self.player_instances.clear()
        for player in players:
            player_inst = models.Player(player["first_name"],
                                        player["last_name"],
                                        player["birthdate"],
                                        player["sex"],
                                        player["ranking"],
                                        id=player["id"],
                                        has_played_with=player["has_played_with"])
            self.player_instances.append(player_inst)
            self.tournament_instance.update_players_list(player_inst)

        # Import rounds & matches data
        self.current_round = len(tournaments[last_tournament]["rounds"])
        for my_round in tournaments[last_tournament]["rounds"]:
            round_inst = models.Round(my_round["name"],
                                      my_round["tournament_id"],
                                      start_datetime=my_round["start_datetime"],
                                      end_datetime=my_round["end_datetime"])

            for match in my_round["matches_list"]:
                p1 = get_player_inst_from_id(match["player1_id"])
                p2 = get_player_inst_from_id(match["player2_id"])
                match_inst = models.Match.create_from_imported_data(
                    p1, p2, match["player1_score"], match["player2_score"])

                round_inst.add_match_to_matches_list(match_inst)

            self.tournament_instance.rounds.append(round_inst)
            self.round_instances.append(round_inst)


class Import_data_menu_controller:
    def __init__(self):
        self.json_files = [file for file in os.listdir('.') if file.endswith('.json')]
        self.view = views.Import_views()
        self.choices = {}
        for num, file in enumerate(self.json_files, start=1):
            self.choices[str(num)] = (self.import_file, file)

    def run(self):
        choice = self.view.import_data(self.json_files)
        action = self.choices.get(choice)
        if action:
            return action[0](action[1])
        else:
            return 'no player', 'no tournament', False

    def import_file(self, file):
        players, tournaments = db.import_data_from_json(file)
        return players.all(), tournaments.all(), True


class Edit_player_menu_controller:
    def __init__(self, players):
        self.view = views.Players_views()
        self.players = players
        self.choices = {}
        for num, player in enumerate(self.players, start=1):
            self.choices[str(num)] = (self.edit_player, player)

    def run(self):
        choice = self.view.edit_players_view(self.players)
        action = self.choices.get(choice)
        if action:
            action[0](action[1])
        else:
            views.Views().wrong_input_view(choice)

    def edit_player(self, player):
        new_ranking = self.view.edit_player_view(player)
        pc = Player_controller(
            [player.first_name, player.last_name, player.birthdate,
             player.sex, new_ranking])
        if pc.is_data_valid():
            player.update_ranking(int(new_ranking))


class Set_matches_results_menu_controller:
    def __init__(self, matches):
        self.view = views.Matches_views()
        self.matches = matches
        self.matches_instances = []
        self.results_set = 0
        self.choices = {}
        for num, match in enumerate(self.matches, start=1):
            self.choices[str(num)] = (self.set_match_result, match)

    def run(self):
        while self.results_set < 4:
            choice = self.view.set_matches_result_view(self.matches)
            action = self.choices.get(choice)
            if action:
                action[0](action[1])
            else:
                views.Views().wrong_input_view(choice)
                self.run()

    def set_match_result(self, match):
        smc = Set_match_result_menu_controller(match)
        match_instance = smc.run()
        self.matches_instances.append(match_instance)
        my_set = set(self.matches_instances)
        self.results_set = len(my_set)


class Set_match_result_menu_controller:
    def __init__(self, match):
        self.view = views.Matches_views()
        self.match = match
        self.choices = {
            "1": (self.set_winner, match.player1),
            "2": (self.set_winner, match.player2),
            "3": (self.set_draw, None)
        }

    def run(self):
        choice = self.view.set_match_result_view(self.match)
        action = self.choices.get(choice)
        if action:
            return action[0](action[1])
        else:
            views.Views().wrong_input_view(choice)
            self.run()

    def set_winner(self, player):
        return self.match.set_results(is_draw=False, winner=player)

    def set_draw(self, _):
        return self.match.set_results(is_draw=True, winner=None)


class Generate_reports_menu_controller:
    def __init__(self):
        self.view = views.Reports_views()
        self.data = db.database
        self.choices = {
            "1": self.get_all_players,
            "2": self.get_players_from_tournament,
            "3": self.get_all_tournaments,
            "4": self.get_rounds_from_tournament,
            "5": self.get_matches_from_tournament
        }

    def run(self):
        choice = self.view.choose_report_view()
        action = self.choices.get(choice)
        if action:
            action()
        else:
            views.Views().wrong_input_view(choice)

    def get_all_players(self):
        self.view.get_all_players_view(self.data.table('players'), None)

    def get_all_tournaments(self):
        self.view.get_all_tournaments_view(self.data.table('tournaments'))

    def get_players_from_tournament(self):
        players_list = self.data.table('players')
        final_list = []
        for tournament in self.data.table('tournaments'):
            tournament_players = tournament["players"]
            for player_id in tournament_players:
                res = [
                    element for element in players_list if element['id'] == player_id]
                final_list.append(res[0])
            self.view.get_all_players_view(final_list, tournament["name"])
            final_list.clear()

    def get_rounds_from_tournament(self):
        final_list = []
        for tournament in self.data.table('tournaments'):
            for my_round in tournament["rounds"]:
                final_list.append(my_round)
            self.view.get_rounds_from_tournament(
                final_list, tournament["name"])
            final_list.clear()

    def get_matches_from_tournament(self):
        match_list = []

        for tournament in self.data.table('tournaments'):
            for my_round in tournament["rounds"]:
                for match in my_round["matches_list"]:
                    match_list.append(match)

            for m in match_list:
                User = db.Query()
                p1 = db.database.table('players').search(
                    User.id == m["player1_id"])
                p2 = db.database.table('players').search(
                    User.id == m["player2_id"])
                m["p1_name"] = p1[0]["first_name"] + ' ' + p1[0]["last_name"]
                m["p2_name"] = p2[0]["first_name"] + ' ' + p2[0]["last_name"]

            self.view.get_matches_from_tournament(
                match_list, tournament["name"])
            match_list.clear()


class Tournament_controller:
    def __init__(self, tournament_data):
        self.tournament_data = tournament_data

    def is_data_valid(self):
        regex_startdate = re.match(
            '^[0-3]?[0-9]/[0-3]?[0-9]/(?:[0-9]{2})?[0-9]{2}$', self.tournament_data[2])
        regex_enddate = re.match(
            '^[0-3]?[0-9]/[0-3]?[0-9]/(?:[0-9]{2})?[0-9]{2}$', self.tournament_data[3])
        if bool(regex_startdate) and bool(regex_enddate):
            # data collected from inputs are valid
            return True
        else:
            views.Views().error_view('Format de date non valide.')


class Player_controller:
    def __init__(self, player_data):
        self.model = models.Player
        self.player_data = player_data

    def is_data_valid(self):
        if self._check_valid_date() and self._check_valid_sex() and self._check_valid_rank():
            return True

    def _check_valid_date(self):
        regex_birthdate = re.match(
            '^[0-3]?[0-9]/[0-3]?[0-9]/(?:[0-9]{2})?[0-9]{2}$', self.player_data[2])
        if bool(regex_birthdate):
            return True
        else:
            views.Views().error_view('Format de date non valide.')

    def _check_valid_sex(self):
        if self.player_data[3].upper() == 'M' or self.player_data[3].upper() == 'F':
            return True
        else:
            views.Views().error_view('Sexe non valide. Veuillez entrer M ou F.')

    def _check_valid_rank(self):
        if self.player_data[4].isdigit():
            if int(self.player_data[4]) > 0:
                return True
        else:
            views.Views().error_view('Votre classement doit être un entier positif.')
