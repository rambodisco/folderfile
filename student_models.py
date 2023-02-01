from config_student import *

class Student(db.Model):
    roll_no = db.Column('Student rollno',db.Integer(),primary_key=True)
    stud_name = db.Column('Student name',db.String(30))
    stud_address = db.Column('Student address',db.String(50))
    Stud_mobile = db.Column('Student mobile',db.String(11),unique=True)
    stud_email = db.Column('Student email',db.String(30),unique=True)
    stud_dept = db.Column('Student department',db.String(20))
    stud_fees = db.Column('Student fees',db.Float())

with app.app_context():
    db.create_all()
    print('Table Created')