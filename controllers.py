from models import *
from views import *


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

print(p1)

'''
players_list = []
p1 = Player('player1', 800)
p2 = Player('player2', 900)
p3 = Player('player3', 80)
p4 = Player('player4', 1200)
p5 = Player('player5', 30)
p6 = Player('player6', 350)
p7 = Player('player7', 120)
p8 = Player('player8', 1800)

p1.points += 0.5
p2.points += 0
p3.points += 0.5
p4.points += 1
p5.points += 0
p6.points += 0.5
p7.points += 1
p8.points += 0.5

players_list.append(p1)
players_list.append(p2)
players_list.append(p3)
players_list.append(p4)
players_list.append(p5)
players_list.append(p6)
players_list.append(p7)
players_list.append(p8)

r = Round('Round 1')

r.generer_paires_next_rounds(players_list)
'''
