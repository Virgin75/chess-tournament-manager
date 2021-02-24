from models import *
from views import *


class Main_menu_controller:
    def __init__(self):
        self.view = Views()
        self.choices = {
            "1": self.create_tournament,
            "2": self.add_player,
            "3": self.edit_player,
            "4": self.start_round,
            "5": self.generate_reports
        }
        self.players_created = 0
        self.player_instances = []
        self.tournament_created = 0
        self.tournament_instance = None
        self.current_round = 0
        self.round_instances = []

    def run(self):
        while True:
            go_to = self.view.main_menu_view(
                self.players_created, self.tournament_created)
            action = self.choices.get(go_to)
            if action:
                action()
            else:
                print(f'{go_to} is not a valid choice')

    def create_tournament(self):
        if self.tournament_created == 0:
            tournament_data = Views().create_tournament_view()
            tc = Tournament_controller(tournament_data)
            if tc.is_data_valid():
                tournament = Tournament(*tournament_data)
                self.view.success_message_tournament(tournament.name)
                self.tournament_created += 1
                self.tournament_instance = tournament
        else:
            '''A tournament has already been created'''
            start_again = self.view.restart_tournament_creation_view()
            if start_again.upper() == "Y":
                self.tournament_created = 0
                self.create_tournament()

    def add_player(self):
        if self.players_created <= 7:
            '''
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

            self.player_instances = [p1, p2, p3, p4, p5, p6, p7, p8]
            self.players_created = 8
            '''
            player_data = Views().create_player_view(self.players_created + 1)
            pc = Player_controller(player_data)
            if pc.is_data_valid():
                player = Player(*player_data)
                self.view.success_message_player(
                    player.first_name, player.last_name)
                self.players_created += 1
                self.player_instances.append(player)
        else:
            '''More than 8 player have already been created'''
            self.view.too_many_players_view()

    def edit_player(self):
        edit_player_controller = Edit_player_menu_controller(
            self.player_instances)
        edit_player_controller.run()

    def start_round(self):

        # The round cannot start if one of the 3 conditions below is met
        if self.players_created < 8:
            return self.view.not_enough_players_view()
        if self.tournament_created == 0:
            return self.view.no_tournamenet_created_view()
        if self.current_round == 4:
            return self.view.no_more_round_view()

        # Start the first round
        if self.current_round == 0:
            round_name = self.view.start_first_round_view()
            first_round = Round(round_name)
            self.round_instances.append(first_round)

            '''Generation des paires'''
            first_round.generer_paires_round1(self.player_instances)
            match_list = first_round.match_instances
            self.view.display_matches_view(match_list)

        # Start the following round
        else:
            pass

        self.current_round += 1

    def generate_reports(self):
        pass


class Edit_player_menu_controller:
    def __init__(self, players):
        self.view = Views()
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
            print(f'{choice} is not a valid choice.')

    def edit_player(self, player):
        new_ranking = self.view.edit_player_view(player)
        pc = Player_controller(
            [player.first_name, player.last_name, player.birthdate,
             player.sex, new_ranking])
        if pc.is_data_valid():
            player.ranking = new_ranking


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
