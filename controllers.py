from models import *
import operator

# tournament_name = input("Nom du tournoi: ")
# tournament_place = input("Lieu du tournoi: ")

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


def generer_paires_round1(players):
    sorted_players = sorted(players, key=operator.attrgetter('ranking'))
    group_inf = sorted_players[:len(sorted_players)//2]
    group_sup = sorted_players[len(sorted_players)//2:]

    paire1 = (group_sup[3], group_inf[3])
    paire2 = (group_sup[2], group_inf[2])
    paire3 = (group_sup[1], group_inf[1])
    paire4 = (group_sup[0], group_inf[0])


def generer_paires_next_rounds(players):
    sorted_players = sorted(
        players, key=operator.attrgetter('points', 'ranking'))

    for player in sorted_players:
        print(f'{player.points}pts - Ranking : {player.ranking}')


generer_paires_next_rounds(players_list)
