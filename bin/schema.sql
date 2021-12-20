DROP TABLE IF EXISTS rounds;
DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS scores;
DROP TABLE IF EXISTS games;

CREATE TABLE games(
    name VARCHAR(20) NOT NULL,
    PRIMARY KEY(name)
);

CREATE TABLE rounds(
    id INTEGER,
    round_number INTEGER,
    game_id VARCHAR(20) NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(game_id) REFERENCES games(name)
);

CREATE TABLE players(
    id INTEGER,
    game_id VARCHAR(20) NOT NULL,
    name VARCHAR(20) NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(game_id) REFERENCES games
);

CREATE TABLE scores(
    id INTEGER,
    game_id VARCHAR(20) NOT NULL,
    round_id INTEGER,
    player_id INTEGER,
    score INTEGER NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(game_id) REFERENCES games(name),
    FOREIGN KEY(round_id) REFERENCES rounds(round_number),
    FOREIGN KEY(player_id) REFERENCES players(id)
);
