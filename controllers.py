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

    group_sup[3].has_played_with.append(group_inf[3])
    group_inf[3].has_played_with.append(group_sup[3])
    group_sup[2].has_played_with.append(group_inf[2])
    group_inf[2].has_played_with.append(group_sup[2])
    group_sup[1].has_played_with.append(group_inf[1])
    group_inf[1].has_played_with.append(group_sup[1])
    group_sup[0].has_played_with.append(group_inf[0])
    group_inf[0].has_played_with.append(group_sup[0])


def generer_paires_next_rounds(players):
    # On trie les joueurs par points puis par rang si même nombre de points
    sorted_players = sorted(
        players, key=operator.attrgetter('points', 'ranking'))

    # Liste de joueurs disponibles (pas encore de paires)
    available_players = sorted_players

    # On génère la paire 1
    if sorted_players[0] not in sorted_players[1].has_played_with:
        paire1 = (sorted_players[0], sorted_players[1])
        available_players.remove(sorted_players[1])
    elif sorted_players[0] not in sorted_players[2].has_played_with:
        paire1 = (sorted_players[0], sorted_players[2])
        available_players.remove(sorted_players[2])
    elif sorted_players[0] not in sorted_players[3].has_played_with:
        paire1 = (sorted_players[0], sorted_players[3])
        available_players.remove(sorted_players[3])
    elif sorted_players[0] not in sorted_players[4].has_played_with:
        paire1 = (sorted_players[0], sorted_players[4])
        available_players.remove(sorted_players[4])
    elif sorted_players[0] not in sorted_players[5].has_played_with:
        paire1 = (sorted_players[0], sorted_players[5])
        available_players.remove(sorted_players[5])
    elif sorted_players[0] not in sorted_players[6].has_played_with:
        paire1 = (sorted_players[0], sorted_players[6])
        available_players.remove(sorted_players[6])
    elif sorted_players[0] not in sorted_players[7].has_played_with:
        paire1 = (sorted_players[0], sorted_players[7])
        available_players.remove(sorted_players[7])
    available_players.remove(sorted_players[0])

    # On génère la paire 2
    if available_players[0] not in available_players[1].has_played_with:
        paire2 = (available_players[0], available_players[1])
        available_players.remove(available_players[1])
    elif available_players[0] not in available_players[2].has_played_with:
        paire2 = (available_players[0], available_players[2])
        available_players.remove(available_players[2])
    elif available_players[0] not in available_players[3].has_played_with:
        paire2 = (available_players[0], available_players[3])
        available_players.remove(available_players[3])
    elif available_players[0] not in available_players[4].has_played_with:
        paire2 = (available_players[0], available_players[4])
        available_players.remove(available_players[4])
    elif available_players[0] not in available_players[5].has_played_with:
        paire2 = (available_players[0], available_players[5])
        available_players.remove(available_players[5])
    available_players.remove(sorted_players[0])

    # On génère la paire 3
    if available_players[0] not in available_players[1].has_played_with:
        paire3 = (available_players[0], available_players[1])
        available_players.remove(available_players[1])
    elif available_players[0] not in available_players[2].has_played_with:
        paire3 = (available_players[0], available_players[2])
        available_players.remove(available_players[2])
    elif available_players[0] not in available_players[3].has_played_with:
        paire3 = (available_players[0], available_players[3])
        available_players.remove(available_players[3])
    available_players.remove(sorted_players[0])

    # On génère la paire 4
    if available_players[0] not in available_players[1].has_played_with:
        paire4 = (available_players[0], available_players[1])
        available_players.remove(available_players[1])
    available_players.remove(sorted_players[0])

    paire1[0].has_played_with.append(paire1[1])
    paire1[1].has_played_with.append(paire1[0])

    paire2[0].has_played_with.append(paire2[1])
    paire2[1].has_played_with.append(paire2[0])

    paire3[0].has_played_with.append(paire3[1])
    paire3[1].has_played_with.append(paire3[0])

    paire4[0].has_played_with.append(paire4[1])
    paire4[1].has_played_with.append(paire4[0])

    print(f'{paire1[0].__str__()} VS {paire1[1].__str__()} \n{paire2[0].__str__()} VS {paire2[1].__str__()} \n{paire3[0].__str__()} VS {paire3[1].__str__()} \n{paire4[0].__str__()} VS {paire4[1].__str__()} \n')
    print([p.__str__() for p in paire1[0].has_played_with])


generer_paires_next_rounds(players_list)
generer_paires_next_rounds(players_list)
generer_paires_next_rounds(players_list)
generer_paires_next_rounds(players_list)
