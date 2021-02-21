from views import *
from controllers import *
from models import *

tc = Tournament_controller()
pc = Player_controller()

tournament = tc.create_tournament()
players = []

for i in range(1, 9):
    players.append(pc.create_player(i))

tournament.players = players
