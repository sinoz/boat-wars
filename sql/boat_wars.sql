DROP TABLE IF EXISTS players;
CREATE TABLE players(
	players_id serial UNIQUE PRIMARY KEY,
	name character varying NOT NULL,
	score integer DEFAULT 0
);

INSERT INTO players (name, score) VALUES ('Mathijs', 3);
INSERT INTO players (name, score) VALUES ('Ryan', 4);
INSERT INTO players (name, score) VALUES ('Johan', 0);
INSERT INTO players (name, score) VALUES ('Sam', 15);
INSERT INTO players (name, score) VALUES ('Xin', 8);
INSERT INTO players (name, score) VALUES ('Maurice', 2);

