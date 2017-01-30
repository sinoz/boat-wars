import db.db_service

name = 'Piet'
wins = 4
losses = 8

db.db_service.execute("INSERT INTO players (name, wins, losses) VALUES (\'" + name + "\', " + str(wins) + ", " + str(losses) + ");")
results = db.db_service.query("SELECT * FROM players")

print(results)