class Tournament:
    def __init__(self, name: str, place: str, date: tuple, description: str, time_control: str, rounds: list, players: list):
        self.name = name
        self.place = place
        self.date = date
        self.description = description
        self.time_control = time_control
        self.nb_rounds = 4
        self.rounds = rounds
        self.players = players


class Player:
    def __init__(self, first_name: str, ranking: int):
        self.first_name = first_name
        # self.last_name = last_name
        # self.birthdate = birthdate
        # self.sex = sex
        self.ranking = ranking  # Postitive int
        self.points = 0

    def __str__(self):
        return f'{self.first_name} - {self.ranking}'


class Match:
    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2
        self.player1_score = 0
        self.player2_score = 0

    def set_results(is_draw: bool, player: Player):
        if is_draw:
            self.player1_score += 0.5
            self.player2_score += 0.5
        if player == self.player1:
            self.player1_score += 1


class Round:
    def __init__(self, name: str, start_datetime: str, end_datetime: str):
        pass
