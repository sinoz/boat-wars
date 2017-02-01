DROP TABLE IF EXISTS players;
CREATE TABLE players(
	players_id serial UNIQUE PRIMARY KEY,
	name character varying NOT NULL,
	wins integer DEFAULT 0,
	losses integer DEFAULT 0
);

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