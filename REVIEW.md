## Review door: Julia Liem

 * Although the code is recognisable from her own project, some parts of `views.py` are still hard to follow/understand.
 The code main goal was to execute properly, but this resulted in a lot of code which gives a bit of a vague impression about what it does.
 More comments would have been helpful.

 * The application makes use of Flask-Login, but only at a background level (the user is "logged in" when he/she creates a game).
 A useful addition might have been to let the user actually create an account, view previous games and winners and maybe even continue previously closed games.