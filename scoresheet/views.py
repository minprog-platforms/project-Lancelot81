from flask import Flask, render_template, request, url_for, redirect, flash, Blueprint
from .models import calculate_score
from flask_login import login_user, login_required, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from .models2 import Game, Round, Player, Score
from . import db


views = Blueprint('views', __name__)


@views.route('/toepen', methods=['GET', 'POST'])
@login_required
def toepen():
    if request.method == 'GET':
        pass

    current_game = current_user.id

    alive_players = Player.query.filter_by(game_id=current_game, status_in=True)

    if request.method == 'POST':
        new_round = Round(round_nm=0, game_id=current_game)
        db.session.add(new_round)
        db.session.commit()

        round_id = Round.query.filter_by(game_id=current_game).first().id

        if request.form.get('add-player') == "Add player":
            player_name = request.form.get('playername')

            exist = Player.query.filter_by(name=player_name, game_id=current_game).first()

            if exist:
                flash('Player already exists.', category='error')
            elif len(player_name) > 19:
                flash("Player name is too long.", category='error')
            else:
                new_player = Player(name=player_name, game_id=current_game, status_in=True)
                db.session.add(new_player)
                db.session.commit()

                player_id = Player.query.filter_by(name=player_name).first().id

                new_score = Score(score=0, game_id=current_game, round_id=round_id, player_id=player_id)
                db.session.add(new_score)
                db.session.commit()



    players = Player.query.filter_by(game_id=current_game).all()
    
    if any(player.scores[0].score != 0 for player in players):
        playing = True
    else:
        playing = False


    return render_template('toep.html', alive=alive_players, players=players, playing=playing, user=current_user)


@views.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.home'))



@views.route('/bridge', methods=['GET', 'POST'])
@login_required
def bridge():
    if request.method == 'GET':
        pass

    current_game = current_user.id

    if request.method == 'POST':
        formdata = request.form

        if request.form.get('add-player') == "Add player":
            player_name = request.form.get('playername')

            exist = Player.query.filter_by(name=player_name, game_id=current_game).first()

            if exist:
                flash('Player already exists.', category='error')
            elif len(player_name) > 19:
                flash("Player name is too long.", category='error')
            else:
                new_player = Player(name=player_name, game_id=current_game)
                db.session.add(new_player)
                db.session.commit()

        if formdata.get('add-round') == "Add round":
            prev_rounds = Round.query.filter_by(game_id=current_game).all()
            next_round_nm = len(prev_rounds) + 1
            new_round = Round(round_nm=next_round_nm, game_id=current_game)
            db.session.add(new_round)
            db.session.commit()

            players = Player.query.filter_by(game_id=current_game).all()
            round_id = Round.query.filter_by(game_id=current_game).all()[-1].id

            for player in players:
                player_id = player.id
                player_name = player.name
                str1 = player_name + 'guess'
                str2 = player_name + 'wins'

                guess = int(formdata.get(str1))
                wins = int(formdata.get(str2))

                player_score = calculate_score(guess, wins)

                new_score = Score(score=player_score, game_id=current_game, round_id=round_id, player_id=player_id)
                db.session.add(new_score)
                db.session.commit()

    players = Player.query.filter_by(game_id=current_game).all()
    rounds = Round.query.filter_by(game_id=current_game).all()
    scores = Score.query.filter_by(game_id=current_game).all()
    totals = {}
    for player in players:
        player_scores = Score.query.filter_by(game_id=current_game, player_id=player.id).all()
        player_score = sum(score.score for score in player_scores)
        totals[player] = player_score

    if rounds == []:
        playing = False
    else:
        playing = True
    
    return render_template('bridge.html', players=players, rounds=rounds, scores=scores, playing=playing, totals=totals, user=current_user)



@views.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        pass

    if request.method == 'POST':
        gamename = request.form.get('gamename')
        gametype = request.form.get('gametype')

        usergame = Game.query.filter_by(name=gamename).first()
        if usergame:
            flash('Game with this name already exists.', category='error')
        elif gamename == "":
            flash('Game name must contain atleast one character.', category='error')
        elif len(gamename) > 19:
            flash("Game name is too long.", category='error')
        else:
            new_game = Game(name=gamename, gametype=gametype)
            db.session.add(new_game)
            db.session.commit()
            flash('Succesfully started a new game.', category='succes')
            logout_user()
            login_user(new_game, remember=True)

            if gametype == 'bridge':
                return redirect(url_for('views.bridge'))
            elif gametype == 'toepen':
                return redirect(url_for('views.toepen'))
    
    return render_template('home.html', user=current_user)

