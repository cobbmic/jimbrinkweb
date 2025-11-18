from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta, datetime

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config["DEBUG"] = True

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(username="jimbrinkweb", password="6#K;8Dtz*6yN<'$k", hostname="jimbrinkweb.mysql.pythonanywhere-services.com", databasename="jimbrinkweb$jimsite")
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299

db = SQLAlchemy(app)

class Lessons(db.Model):

    __tablename__ = "lessons"

    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer)
    lesson_type = db.Column(db.String(15))
    url = db.Column(db.String(150))
    title = db.Column(db.String(80))
    series = db.Column(db.String(80))
    date = db.Column(db.Date())
    info = db.Column(db.String(4096))
    ppt = db.Column(db.String(150))
    manuscript = db.Column(db.String(150))
    handout = db.Column(db.String(150))

info = [
["2011/01/11", "Introduction"],
["2011/02/28", "Invited!"],
["2011/03/21", "Sacred Obsession"],
["2011/04/11", "Puzzled By Paradise"],
["2011/05/08", "Paradise Regained"],
["2011/06/12", "No More"],
["2011/07/25", "Apprehensions of Heaven"],
["2011/08/15", "Beatific Vision"],
["2011/09/11", "Reward!"],
["2011/10/02", "Imagine"]]


lesson_id = 7000

for i in range(1, 11):

    input_lesson_id = lesson_id + i
    input_lesson_type = "Sermon"
    input_url = "http://s3.amazonaws.com/jimbrinkweb/sermons/heaven/heaven{0:02d}.mp3".format(i)
    input_title = info[i-1][1]
    input_series = "Surprised By Hope"
    input_date = info[i-1][0]
    input_info = "Part {0} of Jim's \"Surprised By Hope\" series, also commonly called the \"Heaven\" series.".format(i)
    input_ppt = "http://s3.amazonaws.com/jimbrinkweb/sermons/heaven/heaven{0:02d}.pptx".format(i)
    input_manuscript = "http://s3.amazonaws.com/jimbrinkweb/sermons/heaven/heaven{0:02d}-m.pdf".format(i)
    input_handout = "http://s3.amazonaws.com/jimbrinkweb/sermons/heaven/heaven{0:02d}-h.pdf".format(i)
    
    lesson = Lessons(lesson_id=input_lesson_id, lesson_type=input_lesson_type, url=input_url, title=input_title, series=input_series, date=input_date, info=input_info, ppt=input_ppt, handout=input_handout, manuscript=input_manuscript)
    db.session.add(lesson)
    db.session.commit()
