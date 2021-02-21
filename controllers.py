from models import *
from views import *


class Tournament_controller:
    def __init__(self):
        self.model = Tournament
        self.view = create_tournament_view()

    def create_tournament(self):
        if self._check_valid_dates():
            tournament = self.model(*self.view)
            return tournament
        else:
            # need to start again and input valid dates
            self.view = create_tournament_view()
            self.create_tournament()

    def _check_valid_dates(self):
        regex_startdate = re.match(
            '^[0-3]?[0-9]/[0-3]?[0-9]/(?:[0-9]{2})?[0-9]{2}$', self.view[2])
        regex_enddate = re.match(
            '^[0-3]?[0-9]/[0-3]?[0-9]/(?:[0-9]{2})?[0-9]{2}$', self.view[3])
        if bool(regex_startdate) and bool(regex_enddate):
            return True
        else:
            error_view('Format de date non valide.')


class Player_controller:
    def __init__(self):
        self.model = Player
        self.player_data = []

    def create_player(self, number):
        self.player_data = create_player_view(number)
        if self._check_valid_date() and self._check_valid_sex() and self._check_valid_rank():
            player = Player(*self.player_data)
            success_message(number)
            return player
        else:
            # need to start again and input valid birthdate
            return self.create_player(number)

    def _check_valid_date(self):
        regex_birthdate = re.match(
            '^[0-3]?[0-9]/[0-3]?[0-9]/(?:[0-9]{2})?[0-9]{2}$', self.player_data[2])
        if bool(regex_birthdate):
            return True
        else:
            error_view('Format de date non valide.')

    def _check_valid_sex(self):
        if self.player_data[3].upper() == 'M' or self.player_data[3].upper() == 'F':
            return True
        else:
            error_view('Sexe non valide. Veuillez entrer M ou F.')

    def _check_valid_rank(self):
        if self.player_data[4].isdigit():
            if int(self.player_data[4]) > 0:
                return True
        else:
            error_view('Votre classement doit être un entier positif.')


'''
tournament = Tournament(*create_tournament())
players_data = create_players()

p1 = Player(*players_data[0])
p2 = Player(*players_data[1])
p3 = Player(*players_data[2])
p4 = Player(*players_data[3])
p5 = Player(*players_data[4])
p6 = Player(*players_data[5])
p7 = Player(*players_data[6])
p8 = Player(*players_data[7])

tournament.players = [p1, p2, p3, p4, p5, p6, p7, p8]

first_round = Round(get_round_1_name)
first_round.generer_paires_round1(tournament.players)

print(p1)
'''
