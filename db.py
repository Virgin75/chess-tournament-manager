from tinydb import TinyDB
from tinydb import Query

database = TinyDB('db.json', indent=4, separators=(',', ': '))

players_table = database.table('players')
players_table.truncate()  # clear the table first

tournaments_table = database.table('tournaments')
tournaments_table.truncate()  # clear the table first

query = Query()
