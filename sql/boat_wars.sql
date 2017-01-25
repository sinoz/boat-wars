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