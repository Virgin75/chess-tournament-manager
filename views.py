import re


class Views:
    def main_menu_view(self, nb_players, nb_tournament):
        print('🏆 MENU - Chess Tournament Manager')
        print('------------------------------------')
        if nb_tournament >= 1:
            print('     1 - Create a new tournament --- DONE')
        else:
            print('     1 - Create a new tournament')
        if nb_players:
            print(f'     2 - Add a new player --- {nb_players}/8 added. ')
        else:
            print('     2 - Add a new player')
        print('     3 - Edit a player ranking')
        print('     4 - Start the round')
        print('     5 - Generate reports')
        print('------------------------------------')
        print('Please input a number between 1 & 5 to choose what to do:')
        choice = input('>>> ')

        return choice

    def create_tournament_view(self):
        print('Créez votre tournoi sur Chess Manager 🏆\n -----------------')
        name = input('Nom du tournoi à créer : ')
        place = input('Lieu du tournoi : ')
        start_date = input('Date de début du tounoi (format : JJ/MM/AAAA) : ')
        end_date = input('Date de fin du tounoi (format : JJ/MM/AAAA) : ')
        description = input('Ajoutez une description sur le tournoi : ')
        time_control = input(
            'Contrôle du temps (Bullet / Blitz / Coup rapide) : ')

        return [name, place, start_date, end_date, time_control, description]

    def restart_tournament_creation_view(self):
        print('Un tournoi a déjà été créé...')
        choice = input(
            'Souhaitez-vous recommencer la création du tournoi ? (Y/N) : ')

        return choice

    def create_player_view(self, number):
        if number == 1:
            print('\n ----------------- \n Ajoutez maintenant des joueurs au tournoi :')
        print(f'👤 Ajout Joueur {number}')
        player_first_name = input(
            f'\u001b[33m --Prénom du joueur {number}: \033[0m')
        player_last_name = input(
            f'\u001b[33m --Nom du joueur {number}: \033[0m')
        player_birthdate = input(
            f'\u001b[33m --Date de naissance du joueur {number} (JJ/MM/AAAA) : \033[0m')
        player_sex = input(
            f'\u001b[33m --Sexe du joueur {number} (M/F) : \033[0m')
        player_ranking = input(
            f'\u001b[33m --Classement du joueur {number} (ex: 800) : \033[0m')

        return [player_first_name, player_last_name,
                player_birthdate, player_sex, player_ranking]

    def too_many_players_view(self):
        print('\n - \n Limit of players is set to 8. Tournament is full. \n - \n')

    def edit_player_view(self, players):
        print('------------------------------------')
        for num, player in enumerate(players):
            print(f'{num + 1} - {player.first_name}')
        if players == []:
            print('\n - \n There is no player in the tournament... \n - \n')
        print('------------------------------------')

    def error_view(self, error):
        print(
            f'\u001b[33m\n - \n😞 Erreur lors de la validation des champs : {error}\033[0m\n - \n')
        print('> Veuillez essayer de nouveau...\n')

    def success_message_player(self, f_name, l_name):
        print(f'Joueur "{f_name} {l_name}" ajouté avec succès ✅\n - \033[0m')

    def success_message_tournament(self, title):
        print(f'\n - \nTournoi "{title}" créé avec succès ✅\n - \n\033[0m')

    def get_round_1_name(self):
        print('Avant de commencer la ronde 1, comment souhaitez-vous la nommer ?')
        round_1_name = input('Nom de la ronde 1 (ex : Round 1) : ')

        return round_1_name
