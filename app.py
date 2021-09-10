from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import asc
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///bts.db"
db = SQLAlchemy(app)


class song(db.Model):
    date = db.Column(db.Date)
    song = db.Column(db.String, primary_key=True, nullable=False)
    album = db.Column(db.String)


songs = song.query.order_by(asc(song.date)).all()

temp = 0
index = 0
year = []

for s in songs:
    if index == 0:
        year.append(s.date.year)
        temp = s.date.year
        index = index + 1
    else:
        if temp != s.date.year:
            year.append(s.date.year)
            temp = s.date.year

    # print(type(s.date.year))
# print(s.song)


@app.route('/')
def index():
    return render_template('home.html', songs=songs, year=year)


if __name__ == '__main__':
    app.run()
