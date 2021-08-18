from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import asc
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:je191919@127.0.0.1:3306/bts"
db = SQLAlchemy(app)


class song(db.Model):
    date = db.Column(db.Date)
    song = db.Column(db.String, primary_key=True, nullable=False)
    album = db.Column(db.String)


songs = song.query.order_by(asc(song.date)).all()

# for s in songs:
#print(s.date, '', s.album, '', s.song)
# print(s.song)


@app.route('/')
def index():
    return render_template('home.html', songs=songs)


if __name__ == '__main__':
    app.run()
