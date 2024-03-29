
class Tournament_views:
    def create_tournament_view(self):
        print(
            'Créez votre tournoi sur Chess Manager 🏆\n -----------------')
        name = input(
            'Nom du tournoi à créer : ')
        place = input(
            'Lieu du tournoi : ')
        start_date = input(
            'Date de début du tounoi (format : JJ/MM/AAAA) : ')
        end_date = input(
            'Date de fin du tounoi (format : JJ/MM/AAAA) : ')
        description = input(
            'Ajoutez une description sur le tournoi : ')
        time_control = input(
            'Contrôle du temps (Bullet / Blitz / Coup rapide) : ')

        return [name, place, start_date, end_date, time_control, description]

    def already_created_view(self):
        print("Un tournoi a déjà été créé... Veuillez le terminer avant d'en créer un nouveau.\n")

    def no_tournament_created_view(self):
        print('\n - \n Please input "1" and create a Tournament before starting the first round.. \n - \n')

    def success_message_tournament(self, title):
        print(
            f'\n - \nTournoi "{title}" créé avec succès ✅\n - \n\033[0m')


class Players_views:
    def create_player_view(self, number):
        if number == 1:
            print(
                '\n ----------------- \n Ajoutez maintenant des joueurs au tournoi :')
        print(
            f'👤 Ajout Joueur {number}')
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
        print(
            '\n - \n Limit of players is set to 8. Tournament is full. \n - \n')

    def not_enough_players_view(self):
        print(
            '\n - \n There is not enough players to start the tournament. \n - \n')

    def edit_players_view(self, players):
        print(
            '------------------------------------')
        if players == []:
            print(
                '\n - \n There is no player in the tournament... \n - \n')
        else:
            print(
                '🧍 Here is the list of players in the tournament: \n')
            for num, player in enumerate(players, start=1):
                print(
                    f'{num} - {player.first_name} - Ranked: {player.ranking}')
            print(
                '------------------------------------')
            print(
                'Select a player to edit:')
            choice = input(
                '>>> ')
            print(
                '------------------------------------')

            return choice

    def edit_player_view(self, player):
        print(
            f'What is the new ranking of {player.first_name}')
        print(
            f' - Current ranking: {player.ranking}')
        ranking = input(
            ' - New ranking: ')
        print(
            '------------------------------------')

        return ranking

    def success_message_player(self, f_name, l_name):
        print(
            f'Joueur "{f_name} {l_name}" ajouté avec succès ✅\n - \033[0m')


class Rounds_views:
    def no_more_round_view(self):
        print(
            '\n - \n You just played the last round. No more matches are available. \n - \n')

    def start_round_view(self, round_number):
        print(
            '------------------------------------')
        name = input(
            f'What shoud be the name of the round {round_number + 1}? (ex: Round {round_number + 1}): ')
        print(
            '------------------------------------')

        return name

    def display_matches_view(self, match_list):
        print(
            'Here are the matches of the round: \n')
        for match in match_list:
            print(
                match.__str__())
        print(
            '------------------------------------\n')


class Matches_views:
    def set_matches_result_view(self, matches):

        print(
            '🎉 Select a number to set the result as soon as a game is over: \n')
        for num, match in enumerate(matches, start=1):
            if match.has_results:
                print(
                    f'     {num} - {match} - \u001b[33m Result: {match.player1_score}pts'
                    f'- {match.player2_score}pts\033[0m'
                )
            else:
                print(
                    f'     {num} - {match}')
        print(
            '------------------------------------')
        print(
            'Select a match to set the results:')
        choice = input(
            '>>> ')
        print(
            '------------------------------------\n')

        return choice

    def set_match_result_view(self, match):
        print('What is the result of this match: \n')
        print('------------------------------------\n')
        print(f'        1 - ✅ {match.player1} is the winner.')
        print(f'        2 - ✅ {match.player2} is the winner.')
        print('        3 - There is no winner...')
        choice = input('>>> ')
        print('------------------------------------\n')

        return choice


class Reports_views:
    def choose_report_view(self):
        print('\n📊 Choose a report to display: ')
        print('------------------------------------\n')
        print('        1 - Display all players from all of the tournaments played.')
        print('        2 - Display all players by tournament.')
        print('        3 - Display all the tournaments.')
        print('        4 - Display all the rounds by tournament.')
        print('        5 - Display all the matches by tournament.')
        choice = input('>>> ')
        print('------------------------------------\n')

        return choice

    def get_all_players_view(self, players, tournament_name):
        if len(players) == 0:
            print('There is no player to display.\n')
        else:
            print(
                f'Tournament name: {str(tournament_name)} - Type "A" to sort them by Alphabetical order or'
                f'"R" to sort them by their ranking: ')
            choice = input('>>> ')
            if tournament_name is not None:
                print(f'\nHere is the list of all the players from {tournament_name}: ')
            else:
                print('\nHere is the list of all the players: ')
            print('------------------------------------\n')
            if choice in ('a', 'A'):
                sorted_player = sorted(
                    players,  key=lambda player: player["first_name"])

            elif choice in ('r', 'R'):
                sorted_player = sorted(
                    players,  key=lambda player: player["points"], reverse=True)

            for num, player in enumerate(sorted_player, start=1):
                print(
                    f'   #{num} - {player["first_name"]} {player["last_name"]} ({player["ranking"]})'
                    f' -  {player["points"]}pts')
            print('------------------------------------\n')

    def get_all_tournaments_view(self, tournaments):
        if len(tournaments) == 0:
            print('There is no tournament to display.\n')
        else:
            print(
                '\nHere is the list of all the tournaments: ')
            print(
                '------------------------------------\n')
            for num, tournament in enumerate(tournaments, start=1):
                print(
                    f'     {num} - Name: {tournament["name"]} - Place: {tournament["place"]} -'
                    f'Date: {tournament["start_date"]} > {tournament["end_date"]}. Description: '
                    f'{tournament["description"]} - Time control: {tournament["time_control"]}.'
                )
            print(
                '------------------------------------\n')

    def get_rounds_from_tournament(self, rounds, tournament_name):
        if len(rounds) == 0:
            print('There is no round to display.\n')
        else:
            print(
                f'\nHere is the list of all the rounds in the tournament : {tournament_name}')
            print(
                '------------------------------------\n')
            for num, my_round in enumerate(rounds, start=1):
                print(
                    f'     Round n°{num} - "{my_round["name"]}" - started at: {my_round["start_datetime"]}, '
                    f'ended at: {my_round["end_datetime"]}')
            print(
                '------------------------------------\n')

    def get_matches_from_tournament(self, matches, tournament_name):
        if len(matches) == 0:
            print('There is no match to display.\n')
        else:
            print(
                f'\nHere is the list of all the matches in the tournament : {tournament_name}')
            print(
                '------------------------------------\n')
            for num, match in enumerate(matches, start=1):
                print(
                    f'     {num} - {match["p1_name"]}({match["player1_score"]}) VS '
                    f'{match["p2_name"]}({match["player2_score"]})')
            print(
                '------------------------------------\n')


class Import_views:
    def import_data(self, json_files):
        print('\n💾 Please make sure your .json file to import is located in '
              'the current working directory. \n')
        print('Select a JSON file to import...\n')
        for num, file in enumerate(json_files, start=1):
            print(f'     {num} - {file} ')
        print('------------------------------------')
        choice = input('>>> ')

        return choice


class Views:
    def main_menu_view(self, nb_players, nb_tournament, current_round, tournament_instance, db_name):
        print(
            '\n🏆 MENU - Chess Tournament Manager  ---   ✅ Auto-save to db activated.')
        print(
            '------------------------------------')
        if nb_tournament >= 1:
            print(
                f'     1 -\u001b[33m Create a new tournament\033[0m - -- Tournament: {tournament_instance.name}, '
                f'{tournament_instance.place}')
        else:
            print(
                '     1 - \u001b[33mCreate a new tournament\033[0m')
        if nb_players:
            print(
                f'     2 - \u001b[33mAdd a new player\033[0m --- {nb_players}/8 added. ')
        else:
            print(
                '     2 - \u001b[33mAdd a new player\033[0m')
        print(
            '     3 - \u001b[33mEdit a player ranking\033[0m')
        if current_round == 0:
            print(
                '     4 - \u001b[33mStart the 1st round\033[0m')
        else:
            print(
                f'     4 - \u001b[33mStart the next round\033[0m --- {current_round}/4 round(s) done.')
        print(
            '     5 - \u001b[33mGenerate reports\033[0m')
        print(
            f'     6 - \u001b[33mSwitch database\033[0m --- "{db_name}" file is the active db.')
        print(
            '------------------------------------')
        print(
            'Please input a number between 1 & 6 to choose what to do:')
        choice = input(
            '>>> ')

        return choice

    def wrong_input_view(self, choice):
        print(f'\n❌ {choice} is not a valid choice.\n')

    def error_step_view(self):
        print('\nPlease create a tournament before starting to add players...\n')

    def error_view(self, error):
        print(
            f'\u001b[33m\n - \n😞 Erreur lors de la validation des champs : {error}\033[0m\n - \n')
        print(
            '> Veuillez essayer de nouveau...\n')
