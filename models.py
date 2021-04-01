import operator
from datetime import datetime
import db


class Tournament:
    def __init__(self, name: str, place: str, start_date: str, end_date: str, description: str,
                 time_control: str, **kwargs):
        if 'id' in kwargs:
            self.id = int(kwargs['id'])
        else:
            self.id = id(self)
        self.name = name
        self.place = place
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.time_control = time_control
        self.nb_rounds = 4
        self.rounds = []
        self.players = []  # list of player IDs

    def save_to_db(self):
        db.tournaments_table.insert(self.__dict__)

    def update_players_list(self, player_to_add):
        self.players.append(player_to_add.id)
        tq = db.Query()
        db.tournaments_table.update(
            {'players': self.players}, tq.name == self.name)

    def update_rounds_list(self, round_to_add):
        self.rounds.append(round_to_add)
        tq = db.Query()
        serialized_rounds_list = []
        for ronde in self.rounds:
            serialized_matches_list = []
            for match in ronde.match_instances:

                m = match._serialized_match()
                serialized_matches_list.append(m)

            r = {
                "name": ronde.name,
                "tournament_id": ronde.tournament_id,
                "start_datetime": ronde.start_datetime,
                "end_datetime": ronde.end_datetime,
                "matches_list": serialized_matches_list
            }
            serialized_rounds_list.append(r)
        db.tournaments_table.update(
            {'rounds': serialized_rounds_list}, tq.name == self.name)


class Player:
    def __init__(self, first_name: str, last_name: str, birthdate: str, sex: str, ranking: int, **kwargs):
        if 'id' in kwargs:
            self.id = int(kwargs['id'])
        else:
            self.id = id(self)
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.sex = sex
        self.ranking = int(ranking)
        self.points = 0
        if 'has_played_with' in kwargs:
            self.has_played_with = kwargs['has_played_with']
        else:
            self.has_played_with = []  # list of player IDs

    def update_ranking(self, new_ranking):
        self.ranking = int(new_ranking)
        pq = db.Query()
        db.players_table.update({'ranking': int(new_ranking)}, pq.id ==
                                self.id)

    def update_has_played_with(self, add_player):
        self.has_played_with.append(add_player)
        pq = db.Query()
        db.players_table.update(
            {'has_played_with': self.has_played_with}, pq.id == self.id)

    def save_to_db(self):
        db.players_table.insert(self.__dict__)

    def __str__(self):
        return f'{self.first_name} ({self.ranking})'


class Match:

    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2
        self.player1_score = 0
        self.player2_score = 0
        self.has_results = False
        self.result = ([self.player1, self.player1_score],
                       [self.player2, self.player2_score])

    def set_results(self, is_draw: bool, winner: Player):
        self.player1_score = 0
        self.player2_score = 0
        self.result = ([self.player1, self.player1_score],
                       [self.player2, self.player2_score])
        if is_draw:
            self.player1_score += 0.5
            self.player2_score += 0.5
        if winner == self.player1:
            self.player1_score += 1
        elif winner == self.player2:
            self.player2_score += 1
        self.has_results = True

        self.result = ([self.player1, self.player1_score],
                       [self.player2, self.player2_score])
        return self

    def __str__(self):
        return f'{self.player1} VS {self.player2}'

    def _serialized_match(self):
        serialized_data = {
            "player1_id": self.player1.id,
            "player2_id": self.player2.id,
            "player1_score": self.player1_score,
            "player2_score": self.player2_score,
            "has_results": self.has_results
        }
        return serialized_data


class Round:
    def __init__(self, name: str, tournament_id: int):
        now = datetime.now()
        self.name = name
        self.start_datetime = now.strftime("%d/%m/%Y %H:%M:%S")
        self.end_datetime = ''
        self.match_instances = []
        self.tournament_id = tournament_id

    def set_end_time(self):
        now = datetime.now()
        self.end_datetime = now.strftime("%d/%m/%Y %H:%M:%S")

    def generer_paires_round1(self, players: list):
        sorted_players = sorted(players,  key=lambda player: player.ranking)
        group_inf = sorted_players[:len(sorted_players)//2]
        group_sup = sorted_players[len(sorted_players)//2:]

        paire1 = Match(group_sup[3], group_inf[3])
        paire2 = Match(group_sup[2], group_inf[2])
        paire3 = Match(group_sup[1], group_inf[1])
        paire4 = Match(group_sup[0], group_inf[0])

        self.match_instances = [paire1, paire2, paire3, paire4]

        group_sup[3].update_has_played_with(group_inf[3].id)
        group_inf[3].update_has_played_with(group_sup[3].id)
        group_sup[2].update_has_played_with(group_inf[2].id)
        group_inf[2].update_has_played_with(group_sup[2].id)
        group_sup[1].update_has_played_with(group_inf[1].id)
        group_inf[1].update_has_played_with(group_sup[1].id)
        group_sup[0].update_has_played_with(group_inf[0].id)
        group_inf[0].update_has_played_with(group_sup[0].id)

    def generer_paires_next_rounds(self, players: list):
        # On trie les joueurs par points puis par rang si même nombre de points
        sorted_players = sorted(
            players, key=operator.attrgetter('points', 'ranking'))

        # Liste de joueurs disponibles (pas encore de paires)
        available_players = sorted_players

        # On génère la paire 1
        if sorted_players[0].id not in sorted_players[1].has_played_with:
            paire1 = Match(sorted_players[0], sorted_players[1])
            available_players.remove(sorted_players[1])
        elif sorted_players[0].id not in sorted_players[2].has_played_with:
            paire1 = Match(sorted_players[0], sorted_players[2])
            available_players.remove(sorted_players[2])
        elif sorted_players[0].id not in sorted_players[3].has_played_with:
            paire1 = Match(sorted_players[0], sorted_players[3])
            available_players.remove(sorted_players[3])
        elif sorted_players[0].id not in sorted_players[4].has_played_with:
            paire1 = Match(sorted_players[0], sorted_players[4])
            available_players.remove(sorted_players[4])
        elif sorted_players[0].id not in sorted_players[5].has_played_with:
            paire1 = Match(sorted_players[0], sorted_players[5])
            available_players.remove(sorted_players[5])
        elif sorted_players[0].id not in sorted_players[6].has_played_with:
            paire1 = Match(sorted_players[0], sorted_players[6])
            available_players.remove(sorted_players[6])
        elif sorted_players[0].id not in sorted_players[7].has_played_with:
            paire1 = Match(sorted_players[0], sorted_players[7])
            available_players.remove(sorted_players[7])
        available_players.remove(sorted_players[0])

        # On génère la paire 2
        if available_players[0].id not in available_players[1].has_played_with:
            paire2 = Match(available_players[0], available_players[1])
            available_players.remove(available_players[1])
        elif available_players[0].id not in available_players[2].has_played_with:
            paire2 = Match(available_players[0], available_players[2])
            available_players.remove(available_players[2])
        elif available_players[0].id not in available_players[3].has_played_with:
            paire2 = Match(available_players[0], available_players[3])
            available_players.remove(available_players[3])
        elif available_players[0].id not in available_players[4].has_played_with:
            paire2 = Match(available_players[0], available_players[4])
            available_players.remove(available_players[4])
        elif available_players[0].id not in available_players[5].has_played_with:
            paire2 = Match(available_players[0], available_players[5])
            available_players.remove(available_players[5])
        available_players.remove(sorted_players[0])

        # On génère la paire 3
        if available_players[0].id not in available_players[1].has_played_with:
            paire3 = Match(available_players[0], available_players[1])
            available_players.remove(available_players[1])
        elif available_players[0].id not in available_players[2].has_played_with:
            paire3 = Match(available_players[0], available_players[2])
            available_players.remove(available_players[2])
        elif available_players[0].id not in available_players[3].has_played_with:
            paire3 = Match(available_players[0], available_players[3])
            available_players.remove(available_players[3])
        available_players.remove(sorted_players[0])

        # On génère la paire 4
        if available_players[0].id not in available_players[1].has_played_with:
            paire4 = Match(available_players[0], available_players[1])
            available_players.remove(available_players[1])
        available_players.remove(sorted_players[0])

        paire1.player1.update_has_played_with(paire1.player2.id)
        paire1.player2.update_has_played_with(paire1.player1.id)

        paire2.player1.update_has_played_with(paire2.player2.id)
        paire2.player2.update_has_played_with(paire2.player1.id)

        paire3.player1.update_has_played_with(paire3.player2.id)
        paire3.player2.update_has_played_with(paire3.player1.id)

        paire4.player1.update_has_played_with(paire4.player2.id)
        paire4.player2.update_has_played_with(paire4.player1.id)

        self.match_instances = [paire1, paire2, paire3, paire4]
