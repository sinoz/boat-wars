import db.db_service

def update_highscores(p1, p2, winner):
    player_names = [p1.name, p2.name]
    db_names = db.db_service.query("SELECT name FROM players")

    # Add player data variables
    p1name = player_names[0]
    p2name = player_names[1]

    # If the players have the same name we don't add anything to the database
    if p1name == p2name:
        return

    if winner == p1:
        p1wins = 1
        p2wins = 0
        p1losses = 0
        p2losses = 1
    else:
        p1wins = 0
        p2wins = 1
        p1losses = 1
        p2losses = 0

    # Check if player is already in database
    for db_name in db_names:
        for player_name in player_names:
            if player_name == db_name[0]:
                # Add player 1 data to variables
                if player_name == p1.name:
                    p1data = db.db_service.query("SELECT * FROM players WHERE name = '" + player_name + "'")[0]
                    p1wins += p1data[2]
                    p1losses += p1data[3]
                # Add player 2 data to variables
                else:
                    p2data = db.db_service.query("SELECT * FROM players WHERE name = '" + player_name + "'")[0]
                    p2wins += p2data[2]
                    p2losses += p2data[3]
                # Now we delete the old data from the database
                db.db_service.execute("DELETE FROM players WHERE name = '" + player_name + "'")

    # Insert new player data into database
    db.db_service.execute(
        "INSERT INTO players (name, wins, losses) VALUES ('" + p1name + "', " + str(p1wins) + ", " + str(p1losses) + ");")
    db.db_service.execute(
        "INSERT INTO players (name, wins, losses) VALUES ('" + p2name + "', " + str(p2wins) + ", " + str(p2losses) + ");")

def update_savegame():
    pass