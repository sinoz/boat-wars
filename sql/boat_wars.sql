DROP TABLE IF EXISTS players;
CREATE TABLE players(
	players_id serial UNIQUE PRIMARY KEY,
	name character varying NOT NULL,
	score integer DEFAULT 0
);