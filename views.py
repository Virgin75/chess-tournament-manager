

def create_tournament():
    print('Créez votre tournoi sur Chess Manager 🏆')
    name = input('Nom du tournoi à créer : ')
    place = input('Lieu du tournoi : ')
    start_date = input('Date de début du tounoi (format : JJ/MM/AAAA) : ')
    end_date = input('Date de fin du tounoi (format : JJ/MM/AAAA) : ')
    description = input('Ajoutez une description sur le tournoi : ')
    time_control = input('Contrôle du temps (Bullet / Blitz / Coup rapide) : ')

    return [name, place, start_date, end_date, time_control, description]


def create_players():
    player_list = []
    print('👤 Ajoutez 8 joueurs à ce tournoi...')
    print('Commençons par le joueur 1')
    player1_first_name = input('♐ Prénom du joueur 1: ')
    player1_last_name = input('♐ Nom du joueur 1: ')
    player1_birthdate = input(
        '♐ Date de naissance du joueur 1 (JJ/MM/AAAA) : ')
    player1_sex = input('♐ Sexe du joueur 1 (M/F) : ')
    player1_ranking = input('♐ Classement du joueur 1 (ex: 800) : ')
    print('Joueur 1 ajouté ✅ \nPassons au joueur 2...')
    player_list.append([player1_first_name, player1_last_name,
                        player1_birthdate, player1_sex, player1_ranking])

    player2_first_name = input('♓ Prénom du joueur 2: ')
    player2_last_name = input('♓ Nom du joueur 2: ')
    player2_birthdate = input(
        '♓ Date de naissance du joueur 2 (JJ/MM/AAAA) : ')
    player2_sex = input('♓ Sexe du joueur 2 (M/F) : ')
    player2_ranking = input('♓ Classement du joueur 2 (ex: 800) : ')
    print('Joueur 2 ajouté ✅ \nPassons au joueur 3...')
    player_list.append([player2_first_name, player2_last_name,
                        player2_birthdate, player2_sex, player2_ranking])

    player3_first_name = input('♈ Prénom du joueur 3: ')
    player3_last_name = input('♈ Nom du joueur 3: ')
    player3_birthdate = input(
        '♈ Date de naissance du joueur 3 (JJ/MM/AAAA) : ')
    player3_sex = input('♈ Sexe du joueur 3 (M/F) : ')
    player3_ranking = input('♈ Classement du joueur 3 (ex: 800) : ')
    print('Joueur 3 ajouté ✅ \nPassons au joueur 4...')
    player_list.append([player3_first_name, player3_last_name,
                        player3_birthdate, player3_sex, player3_ranking])

    player4_first_name = input('♍ Prénom du joueur 4: ')
    player4_last_name = input('♍ Nom du joueur 4: ')
    player4_birthdate = input(
        '♍ Date de naissance du joueur 4 (JJ/MM/AAAA) : ')
    player4_sex = input('♍ Sexe du joueur 4 (M/F) : ')
    player4_ranking = input('♍ Classement du joueur 4 (ex: 800) : ')
    print('Joueur 4 ajouté ✅ \nPassons au joueur 5...')
    player_list.append([player4_first_name, player4_last_name,
                        player4_birthdate, player4_sex, player4_ranking])

    player5_first_name = input('♌ Prénom du joueur 5: ')
    player5_last_name = input('♌ Nom du joueur 5: ')
    player5_birthdate = input(
        '♌ Date de naissance du joueur 5 (JJ/MM/AAAA) : ')
    player5_sex = input('♌ Sexe du joueur 5 (M/F) : ')
    player5_ranking = input('♌ Classement du joueur 5 (ex: 800) : ')
    print('Joueur 5 ajouté ✅ \nPassons au joueur 6...')
    player_list.append([player5_first_name, player5_last_name,
                        player5_birthdate, player5_sex, player5_ranking])

    player6_first_name = input('♒ Prénom du joueur 6: ')
    player6_last_name = input('♒ Nom du joueur 6: ')
    player6_birthdate = input(
        '♒ Date de naissance du joueur 6 (JJ/MM/AAAA) : ')
    player6_sex = input('♒ Sexe du joueur 6 (M/F) : ')
    player6_ranking = input('♒ Classement du joueur 6 (ex: 800) : ')
    print('Joueur 6 ajouté ✅ \nPassons au joueur 7...')
    player_list.append([player6_first_name, player6_last_name,
                        player6_birthdate, player6_sex, player6_ranking])

    player7_first_name = input('♋ Prénom du joueur 7: ')
    player7_last_name = input('♋ Nom du joueur 7: ')
    player7_birthdate = input(
        '♋ Date de naissance du joueur 7 (JJ/MM/AAAA) : ')
    player7_sex = input('♋ Sexe du joueur 7 (M/F) : ')
    player7_ranking = input('♋ Classement du joueur 7 (ex: 800) : ')
    print('Joueur 7 ajouté ✅ \nPassons au joueur 8...')
    player_list.append([player7_first_name, player7_last_name,
                        player7_birthdate, player7_sex, player7_ranking])

    player8_first_name = input('♋ Prénom du joueur 8: ')
    player8_last_name = input('♋ Nom du joueur 8: ')
    player8_birthdate = input(
        '♋ Date de naissance du joueur 8 (JJ/MM/AAAA) : ')
    player8_sex = input('♋ Sexe du joueur 8 (M/F) : ')
    player8_ranking = input('♋ Classement du joueur 8 (ex: 800) : ')
    print('Joueur 8 ajouté ✅')
    player_list.append([player8_first_name, player8_last_name,
                        player8_birthdate, player8_sex, player8_ranking])

    return player_list
