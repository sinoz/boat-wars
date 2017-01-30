DROP TABLE IF EXISTS players;
CREATE TABLE players(
	players_id serial UNIQUE PRIMARY KEY,
	name character varying NOT NULL,
	score integer DEFAULT 0
);

ALTER TABLE players
RENAME COLUMN score to wins;

ALTER TABLE players
ADD losses integer;

INSERT INTO players (name, wins, losses) VALUES ('Mathijs', 21, 20);
INSERT INTO players (name, wins, losses) VALUES ('Ryan', 10, 11);
INSERT INTO players (name, wins, losses) VALUES ('Johan', 7, 7);
INSERT INTO players (name, wins, losses) VALUES ('Sam', 15, 18);
INSERT INTO players (name, wins, losses) VALUES ('Xin', 8, 6);
INSERT INTO players (name, wins, losses) VALUES ('Maurice', 24, 30);


DROP TABLE IF EXISTS Boats;
CREATE TABLE Boats(
    XPos integer,
    YPos integer,
    HP integer,
    BID varchar(10),
    State varchar(10),
    BRange integer,
    Attack integer,
    ShotDef boolean,
    MineDef boolean,
    ReflDef boolean,
    BoatMovementLeft integer
);

DROP TABLE IF EXISTS Cards;
CREATE TABLE Cards(
    CName varchar(10),
    CType varchar(10),
    CLang varchar(10)
);

DROP TABLE IF EXISTS Turn;
CREATE TABLE Turn(
    Turn integer
);