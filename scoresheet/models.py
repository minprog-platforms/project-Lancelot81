"""
Defines python classes for the database.
Defines a score function for the bridge game.
"""

from . import db
from flask_login import UserMixin


# Class containing a game, a game contains both rounds and players through a class-relationship
class Game(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    gametype = db.Column(db.String(6))
    rounds = db.relationship('Round', cascade="all, delete")
    players = db.relationship('Player', cascade="all, delete")


# Class containing a round of a game
class Round(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    round_nm = db.Column(db.Integer)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'))
    scores = db.relationship('Score', cascade="all, delete")


# Class which will contain the player of a game
class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    status_in = db.Column(db.Boolean, default=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'))
    scores = db.relationship('Score', cascade="all, delete")


# Class containing a score for a player in round of game
class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer, default=0)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'))
    round_id = db.Column(db.Integer, db.ForeignKey('round.id'))
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'))


# Calculates score based on guess and wins
def calculate_score(guess, wins):
    if guess == wins:
        return 6 + guess * 2
    elif guess > wins:
        return (wins - guess) * 2
    else:
        return (guess - wins) * 2
