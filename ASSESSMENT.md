The code of my project has seen a lot of different forms during development.
At first, I started building a static website which used JavaScript to keep track of scores.
After I decided that I wanted to have a database behind my website, I spent a lot of time building a Flask application around my already existing HTML and JS. Even the database has seen different form. I started by using sqlite3, but ended up using python classes and the SQLAlchemy module from flask.
In the end I wonder if I should have added more features to interact with the databse, but at least progress will not be lost when one accidentally closes the tab (refreshing or restoring the tab with `Ctrl + Shift + T` will refresh the old data).
Getting the docker application to work with flask took some time, but I am glad to say it does and I am proud to say that the application runs smoothly on the webserver.
