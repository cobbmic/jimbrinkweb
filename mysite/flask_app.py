from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_basicauth import BasicAuth
from time import strftime

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config["DEBUG"] = True

# password for BasicAuth
app.config['BASIC_AUTH_USERNAME'] = 'acsc'
app.config['BASIC_AUTH_PASSWORD'] = 'alumni'
basic_auth = BasicAuth(app)

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

class Impact(db.Model):
    __tablename__ = "impact"
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(32))
    first_name = db.Column(db.String(32))
    comment = db.Column(db.String(10000))
    date = db.Column(db.Date())

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/baptism-article')
def bap_art():
    return render_template("baptism-article.html")

@app.route('/cc-interview')
def cc_int():
    return render_template("cc-interview.html")

@app.route('/articles')
def article():
    return render_template("articles.html")

@app.route('/lessons')
def lessons():
    return render_template("lessons.html", lessons=Lessons.query.all())

@app.route('/add_lesson', methods=["GET","POST"])
@basic_auth.required
def add_lesson():
    if request.method == "GET":
        return render_template("add_lesson.html")

    lesson = Lessons(url=request.form["inputURL"], title=request.form["inputTitle"], series=request.form["inputSeries"], date=request.form["inputDate"], info=request.form["inputInfo"], lesson_id=request.form["inputID"], lesson_type=request.form["inputType"], ppt=request.form["inputPPT"], manuscript=request.form["inputManuscript"], handout=request.form["inputHandout"])
    db.session.add(lesson)
    db.session.commit()
    return redirect(url_for('add_lesson'))

@app.route('/add_impact', methods=["GET", "POST"])
@basic_auth.required
def add_impact():
    if request.method == "GET":
        return render_template("add_impact.html")

    impact = Impact(last_name=request.form["inputLast"], first_name=request.form["inputFirst"], comment=request.form["inputComment"], date=strftime('%Y-%m-%d'))
    db.session.add(impact)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/welldone')
def welldone():
    return render_template("welldone.html")

@app.route('/impact')
def impact():
    return render_template("impact.html", impacts=Impact.query.all())
