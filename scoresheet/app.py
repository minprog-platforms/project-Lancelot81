from flask import Flask, render_template, request, url_for, redirect, flash, Blueprint
from models import get_players, get_rounds, create_round, create_score, calculate_score, add_player, add_game, get_game
from flask_login import login_user, login_required, logout_user, current_user, LoginManager
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine


db = automap_base()

# engine, suppose it has two tables 'user' and 'address' set up
engine = create_engine("sqlite:///database.db")

# reflect the tables
db.prepare(engine, reflect=True)

# mapped classes are now created with names by default
# matching that of the table name.
Games = db.classes.games
Rounds = db.classes.rounds
Players = db.classes.players
Scores = db.classes.scores

session = Session(engine)

login_manager = LoginManager()
login_manager.login_view = 'app.home'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(text):
    return get_game(text)



@app.route('/game', methods=['GET', 'POST'])
@login_required
def index():
    if request.method == 'GET':
        pass

    
    players = get_players(gamename)

    if request.method == 'POST':
        if request.form.get('add-btn') == "Add player":
            gamename = request.form.get('gamename')
            player_name = request.form.get('playername')
            add_player(gamename, player_name)

        if request.form.get('add-btn') == "Add round":
            gamename = request.form.get('gamename')
            round_id = create_round(gamename)

            for player in players:
                player_id = player[0]
                player_name = player[1]

                guess = request.form.get(player_name + 'guess')
                wins = request.form.get(player_name + 'wins')

                player_score = calculate_score(guess, wins)

                create_score(gamename, round_id, player_id, player_score)

    try:
        rounds = get_rounds(gamename, players)
    except:
        rounds = []

    
    return render_template('index.html', user=current_user)



@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        pass

    if request.method == 'POST':
        gamename = request.form.get('gamename')

        usergame = session.query(Games).filter_by(name=gamename).first()
        if not usergame:
            flash('Game with this name already exists.', category='error')
        else:
            add_game(gamename)
            login_user(usergame, remember=True)
            return redirect(url_for('app.home'))
    
    return render_template('home.html')

