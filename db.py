from tinydb import TinyDB
from tinydb import Query

database = TinyDB('db.json', indent=4, separators=(',', ': '))
database.default_table_name = 'db.json'

players_table = database.table('players')
players_table.truncate()  # clear the table first

tournaments_table = database.table('tournaments')
tournaments_table.truncate()  # clear the table first


def import_data_from_json(file):
    global database
    database = TinyDB(file, indent=4, separators=(',', ': '))
    global players_table
    global tournaments_table
    players_table = database.table('players')
    tournaments_table = database.table('tournaments')
    database.default_table_name = file

    return players_table, tournaments_table


query = Query()
