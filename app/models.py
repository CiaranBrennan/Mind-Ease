from app import db

studentModule = db.Table('studentModule',
    db.Column('module_id', db.Integer, db.ForeignKey('lectures.lecture_id')),
    db.Column('user_id', db.Integer, db.ForeignKey('users.user_id'))
)

class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), index=True)
    password = db.Column(db.String(32))
    modules = db.relationship('Lectures', secondary=studentModule,\
        backref=db.backref('users', lazy=True))

class Lectures(db.Model):
    lecture_id = db.Column(db.Integer, primary_key=True)
    module = db.Column(db.String(64))
    grade = db.Column(db.Integer)
    attendance = db.Column(db.Integer)

class Appointments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student = db.Column(db.String(20), index=True)
    date = db.Column(db.Date)
    time = db.Column(db.Time)
