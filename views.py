import re


def create_tournament_view():
    print('Créez votre tournoi sur Chess Manager 🏆\n -----------------')
    name = input('Nom du tournoi à créer : ')
    place = input('Lieu du tournoi : ')
    start_date = input('Date de début du tounoi (format : JJ/MM/AAAA) : ')
    end_date = input('Date de fin du tounoi (format : JJ/MM/AAAA) : ')
    description = input('Ajoutez une description sur le tournoi : ')
    time_control = input('Contrôle du temps (Bullet / Blitz / Coup rapide) : ')

    return [name, place, start_date, end_date, time_control, description]


def create_player_view(number):
    if number == 1:
        print('\n ----------------- \n Ajoutez maintenant des joueurs au tournoi :')
    print(f'👤 Ajout Joueur {number}')
    player_first_name = input(
        f'\u001b[33m --Prénom du joueur {number}: \033[0m')
    player_last_name = input(f'\u001b[33m --Nom du joueur {number}: \033[0m')
    player_birthdate = input(
        f'\u001b[33m --Date de naissance du joueur {number} (JJ/MM/AAAA) : \033[0m')
    player_sex = input(f'\u001b[33m --Sexe du joueur {number} (M/F) : \033[0m')
    player_ranking = input(
        f'\u001b[33m --Classement du joueur {number} (ex: 800) : \033[0m')

    return [player_first_name, player_last_name,
            player_birthdate, player_sex, player_ranking]


def error_view(error):
    print(
        f'😞 Erreur lors de la validation des champs : {error}\n Veuillez recommencer ci-dessous :\n - \n')


def success_message(number):
    print(f'Joueur {number} ajouté ✅\n - \033[0m')


def get_round_1_name():
    print('Avant de commencer la ronde 1, comment souhaitez-vous la nommer ?')
    round_1_name = input('Nom de la ronde 1 (ex : Round 1) : ')

    return round_1_name
