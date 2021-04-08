from tinydb import TinyDB
from tinydb import Query
from datetime import datetime

db_name = 'db.json'

try:
    f = open(db_name)
    # le fichier db.json existe, alors on en créé un nouveau pour ne pas l'écraser
    db_name = f'db-{datetime.now().timestamp()}.json'
    f.close()
except IOError:
    # Le fichier db.json n'existe pas
    db_name = 'db.json'

database = TinyDB(db_name, indent=4, separators=(',', ': '))
database.default_table_name = db_name

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
