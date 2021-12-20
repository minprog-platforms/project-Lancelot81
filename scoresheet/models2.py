from . import db
from flask_login import UserMixin


class Game(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True)
    gametype = db.Column(db.String(6))
    rounds = db.relationship('Round', cascade="all, delete")
    players = db.relationship('Player', cascade="all, delete")


class Round(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    round_nm = db.Column(db.Integer)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'))
    scores = db.relationship('Score', cascade="all, delete")


class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    status_in = db.Column(db.Boolean, default=True)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'))
    scores = db.relationship('Score', cascade="all, delete")


class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer, default=0)
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'))
    round_id = db.Column(db.Integer, db.ForeignKey('round.id'))
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    