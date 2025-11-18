from app import db

class Lessons(db.Model):

    __tablename__ = "lessons"

    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer)
    lesson_type = db.Column(db.String(15))
    url = db.Column(db.String(150))
    title = db.Column(db.String(80))
    series = db.Column(db.String(80))
    date = db.Column(db.Date())
    desc = db.Column(db.String(4096))
    ppt = db.Column(db.String(150))
    manuscript = db.Column(db.String(150))
    handout = db.Column(db.String(150))
