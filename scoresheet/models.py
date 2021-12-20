# import sqlite3 as sql
# from os import path

# ROOT = path.dirname(path.relpath((__file__)))

# # Adds a game to the games table
# def add_game(gamename):
#     con = sql.connect(path.join(ROOT, 'database.db'))
#     cur = con.cursor()
#     cur.execute('INSERT INTO games (name) VALUES(?)', [gamename])
#     con.commit()
#     con.close()


# # Get a game
# def get_game(text):
#     con = sql.connect(path.join(ROOT, 'database.db'))
#     cur = con.cursor()
#     cur.execute('SELECT * FROM games WHERE name = ?', [text])
#     gameref = cur.fetchall()
#     return gameref


# # Adds a player to the players table
# def add_player(gamename, playername):
#     con = sql.connect(path.join(ROOT, 'database.db'))
#     cur = con.cursor()
#     cur.execute('INSERT INTO players (game_id, name) VALUES(?, ?)', [gamename, playername])
#     con.commit()
#     con.close()


# # Gets all player(id, name) from players table
# def get_players(gamename):
#     con = sql.connect(path.join(ROOT, 'database.db'))
#     cur = con.cursor()
#     cur.execute('SELECT (id, name) FROM players WHERE game_id = ?', [gamename])
#     players = cur.fetchall()
#     return players


# # Creates a new round
# def create_round(gamename):
#     con = sql.connect(path.join(ROOT, 'database.db'))
#     cur = con.cursor()
#     cur.execute('SELECT * FROM rounds WHERE game_id = ?', [gamename])
#     new_round_nm = len(cur.fetchall()) + 1
#     cur = con.cursor()
#     cur.execute('INSERT INTO rounds (round_number, game_id) VALUES(?, ?)', [new_round_nm, gamename])
#     con.commit()
#     con.close()


# Calculates score based on guess and wins
def calculate_score(guess, wins):
    if guess == wins:
        return 6 + guess * 2
    elif guess > wins:
        return (wins - guess) * 2
    else:
        return (guess - wins) * 2
    

# # Adds player score to the table
# def create_score(gamename, round_id, player_id, score):
#     con = sql.connect(path.join(ROOT, 'database.db'))
#     cur = con.cursor()
#     cur.execute('INSERT INTO scores (game_id, round_id, player_id, score) VALUES(?, ?, ?, ?)', [gamename, round_id, player_id, score])
#     con.commit()
#     con.close()


# # Gets all scores for every round
# def get_rounds(gamename, players):
#     con = sql.connect(path.join(ROOT, 'database.db'))
#     cur = con.cursor()

#     # get all round id's
#     cur.execute('SELECT * FROM rounds WHERE game_id = ?', [gamename])
#     rounds = cur.fetchall()

#     cur = con.cursor()
#     all_round_scores = []

#     # for each round get all scores
#     for round in rounds:
#         round_scores = []

#         for i in range(1, len(players) + 1):
#             cur.execute('SELECT (score) FROM scores WHERE round_id = ? AND player_id = ? AND game_id = ?', [round, i, gamename])
#             player_score = cur.fetchall()
#             round_scores.append(player_score[0])
        
#         all_round_scores.append(round_scores)

#     return all_round_scores

