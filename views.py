import re


class Views:
    def main_menu_view(self, nb_players, nb_tournament):
        print('🏆 MENU - Chess Tournament Manager')
        print('------------------------------------')
        if nb_tournament >= 1:
            print(
                '    1 - \u001b[33m Create a new tournament\033[0m --- DONE')
        else:
            print('     1 - \u001b[33mCreate a new tournament\033[0m')
        if nb_players:
            print(
                f'     2 - \u001b[33mAdd a new player\033[0m --- {nb_players}/8 added. ')
        else:
            print('     2 - \u001b[33mAdd a new player\033[0m')
        print('     3 - \u001b[33mEdit a player ranking\033[0m')
        print('     4 - \u001b[33mStart the round\033[0m')
        print('     5 - \u001b[33mGenerate reports\033[0m')
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

    def not_enough_players_view(self):
        print('\n - \n There is not enough players to start the tournament. \n - \n')

    def no_tournamenet_created_view(self):
        print('\n - \n Please input "1" and create a Tournament before starting the first round.. \n - \n')

    def edit_players_view(self, players):

        print('------------------------------------')
        if players == []:
            print('\n - \n There is no player in the tournament... \n - \n')
        else:
            print('🧍 Here is the list of players: \n')
            for num, player in enumerate(players, start=1):
                print(f'{num} - {player.first_name} - Ranked: {player.ranking}')
            print('------------------------------------')
            print('Select a player to edit:')
            choice = input('>>> ')
            print('------------------------------------')

            return choice

    def edit_player_view(self, player):
        print(f'What is the new ranking of {player.first_name}')
        print(f' - Current ranking: {player.ranking}')
        ranking = input(' - New ranking: ')
        print('------------------------------------')

        return ranking

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
