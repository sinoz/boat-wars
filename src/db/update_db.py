import db.db_service

def update_highscores(p1, p2):
    p1name = p1.name
    p2name = p2.name
    names = db.db_service.query("SELECT name FROM players")

    for name in names:
        if name == p1:
            p1data = db.db_service.execute("SELECT * FROM players WHERE name = " + name)
    db.db_service.execute("INSERT INTO players(" + p1name + ", ")

    for name in names:
        if name == p2:
            pass


def update_gamestate():
    pass