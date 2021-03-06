from models import *
from views import *
from db import *


class Main_menu_controller:
    def __init__(self):
        self.view = Views()
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

        ''' delete after this line - dummy data'''
        p1 = Player(*['Pedrito', 'player_last_name',
                      '11/11/1111', 'm', 333])
        p2 = Player(*['Paolo', 'player_last_name',
                      '11/11/1111', 'm', 233])
        p3 = Player(*['Poberta', 'player_last_name',
                      '11/11/1111', 'm', 1303])
        p4 = Player(*['Flabu', 'player_last_name',
                      '11/11/1111', 'm', 23])
        p5 = Player(*['Kaku', 'player_last_name',
                      '11/11/1111', 'm', 3])
        p6 = Player(*['Toto', 'player_last_name',
                      '11/11/1111', 'm', 812])
        p7 = Player(*['Pipi', 'player_last_name',
                      '11/11/1111', 'm', 13])
        p8 = Player(*['Popo', 'player_last_name',
                      '11/11/1111', 'm', 120])
        p1.save_to_db()
        p2.save_to_db()
        p3.save_to_db()
        p4.save_to_db()
        p5.save_to_db()
        p6.save_to_db()
        p7.save_to_db()
        p8.save_to_db()

        self.player_instances = [p1, p2, p3, p4, p5, p6, p7, p8]
        self.players_created = 8
        self.tournament_created = 1
        self.tournament_instance = Tournament(
            'fdfd', 'Paris', '11/11/1111', '11/11/1111', 'desc', 'blitz')
        self.tournament_instance.save_to_db()
        self.tournament_instance.update_players_list(p1)
        self.tournament_instance.update_players_list(p2)
        self.tournament_instance.update_players_list(p3)
        self.tournament_instance.update_players_list(p4)
        self.tournament_instance.update_players_list(p5)
        self.tournament_instance.update_players_list(p6)
        self.tournament_instance.update_players_list(p7)
        self.tournament_instance.update_players_list(p8)

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
                self.players_created, self.tournament_created, self.current_round, self.tournament_instance)
            action = self.choices.get(go_to)
            if action:
                action()
            else:
                print(f'{go_to} is not a valid choice')

    def create_tournament(self):
        if self.tournament_created == 0:
            tournament_data = Tournament_views().create_tournament_view()
            tc = Tournament_controller(tournament_data)
            if tc.is_data_valid():
                tournament = Tournament(*tournament_data)
                Tournament_views().success_message_tournament(tournament.name)
                self.tournament_created += 1
                self.tournament_instance = tournament
                tournament.save_to_db()
        else:
            '''A tournament has already been created'''
            Tournament_views().already_created_view()

    def add_player(self):
        if self.players_created <= 7:
            player_data = Players_views().create_player_view(self.players_created + 1)
            pc = Player_controller(player_data)
            if pc.is_data_valid():
                player = Player(*player_data)
                Players_views().success_message_player(
                    player.first_name, player.last_name)
                self.players_created += 1
                self.player_instances.append(player)
                player.save_to_db()
                self.tournament_instance.update_players_list(player)
        else:
            '''More than 8 player have already been created'''
            Players_views().too_many_players_view()

    def edit_player(self):
        edit_player_controller = Edit_player_menu_controller(
            self.player_instances)
        edit_player_controller.run()

    def start_round(self):
        # The round cannot start if one of the 3 conditions below is met
        if self.players_created < 8:
            return Players_views().not_enough_players_view()
        if self.tournament_created == 0:
            return Tournament_views().no_tournament_created_view()
        if self.current_round == 4:
            return Rounds_views().no_more_round_view()

        round_name = Rounds_views().start_round_view(self.current_round)
        my_round = Round(round_name, self.tournament_instance.id)
        self.round_instances.append(my_round)

        # Generate paires first round
        if self.current_round == 0:
            my_round.generer_paires_round1(self.player_instances)

        # Generate paires following rounds
        else:
            my_round.generer_paires_next_rounds(self.player_instances)

        match_list = my_round.match_instances
        Rounds_views().display_matches_view(match_list)

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
        pass


class Edit_player_menu_controller:
    def __init__(self, players):
        self.view = Views()
        self.players = players
        self.choices = {}
        for num, player in enumerate(self.players, start=1):
            self.choices[str(num)] = (self.edit_player, player)

    def run(self):
        choice = Players_views().edit_players_view(self.players)
        action = self.choices.get(choice)
        if action:
            action[0](action[1])
        else:
            print(f'{choice} is not a valid choice.')

    def edit_player(self, player):
        new_ranking = Players_views().edit_player_view(player)
        pc = Player_controller(
            [player.first_name, player.last_name, player.birthdate,
             player.sex, new_ranking])
        if pc.is_data_valid():
            player.update_ranking(int(new_ranking))


class Set_matches_results_menu_controller:
    def __init__(self, matches):
        self.view = Views()
        self.matches = matches
        self.matches_instances = []
        self.results_set = 0
        self.choices = {}
        for num, match in enumerate(self.matches, start=1):
            self.choices[str(num)] = (self.set_match_result, match)

    def run(self):
        while self.results_set < 4:
            choice = Matches_views().set_matches_result_view(self.matches)
            action = self.choices.get(choice)
            if action:
                action[0](action[1])
            else:
                print(f'{choice} is not a valid choice.')
                self.run()

    def set_match_result(self, match):
        smc = Set_match_result_menu_controller(match)
        match_instance = smc.run()
        self.matches_instances.append(match_instance)
        my_set = set(self.matches_instances)
        self.results_set = len(my_set)


class Set_match_result_menu_controller:
    def __init__(self, match):
        self.view = Views()
        self.match = match
        self.choices = {
            "1": (self.set_winner, match.player1),
            "2": (self.set_winner, match.player2),
            "3": (self.set_draw, None)
        }

    def run(self):
        choice = Matches_views().set_match_result_view(self.match)
        action = self.choices.get(choice)
        if action:
            return action[0](action[1])
        else:
            print(f'{choice} is not a valid choice.')
            self.run()

    def set_winner(self, player):
        return self.match.set_results(is_draw=False, winner=player)

    def set_draw(self, _):
        return self.match.set_results(is_draw=True, winner=None)


class Edit_player_menu_controller:
    def __init__(self, players):
        self.players = players
        self.choices = {}
        for num, player in enumerate(self.players, start=1):
            self.choices[str(num)] = (self.edit_player, player)

    def run(self):
        choice = Players_views().edit_players_view(self.players)
        action = self.choices.get(choice)
        if action:
            action[0](action[1])
        else:
            print(f'{choice} is not a valid choice.')

    def edit_player(self, player):
        new_ranking = Players_views().edit_player_view(player)
        pc = Player_controller(
            [player.first_name, player.last_name, player.birthdate,
             player.sex, new_ranking])
        if pc.is_data_valid():
            nr = int(new_ranking)
            player.update_ranking(nr)


class Generate_reports_menu_controller:
    def __init__(self):
        self.view = Reports_views()
        self.data = database
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
            print(f'{choice} is not a valid choice.')

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
        pass

    def get_matches_from_tournament(self):
        pass


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
            Views().error_view('Format de date non valide.')


class Player_controller:
    def __init__(self, player_data):
        self.model = Player
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
            Views().error_view('Format de date non valide.')

    def _check_valid_sex(self):
        if self.player_data[3].upper() == 'M' or self.player_data[3].upper() == 'F':
            return True
        else:
            Views().error_view('Sexe non valide. Veuillez entrer M ou F.')

    def _check_valid_rank(self):
        if self.player_data[4].isdigit():
            if int(self.player_data[4]) > 0:
                return True
        else:
            Views().error_view('Votre classement doit être un entier positif.')
