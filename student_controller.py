from student_models import *
from flask import render_template,request


@app.route('/')
def wellcome_page():
    return render_template('index.html')

@app.route('/add-stud',methods=['GET'])
@app.route('/stud-save',methods=['GET','POST'])
def add_student():
    if request.method == 'POST':
        formdata = request.form
        print(formdata)

        errors = []
        if not formdata.get('sname'):
            errors.append('Student Cannot be Empty')
        if not formdata.get('saddress'):
            errors.append('address Cannot be Empty')
        if not formdata.get('smobile'):
            errors.append('mobile no Cannot Be Empty')
        if not formdata.get('semail'):
            errors.append('Email Cannot be Empty')
        if not formdata.get('sfees'):
            errors.append('Fees Cannot be Empty')

        else:
            try:
                stud_fees = float(formdata.get('sfees'))
                if stud_fees<=0:
                    errors.append('Invalid Fees')
            except:
                errors.append('Invalid Fees')

        if errors:
            return render_template('addstudent.html',smessage=errors)
    student = Student(roll_no = formdata.get('rno'), stud_name=formdata.get('sname'), stud_fees=stud_fees, stud_mobile=formdata.get('smobile'),
                        stud_dept=formdata.get('sdept'), stud_address=formdata.get('saddress'), stud_email=formdata.get('semail'))
    db.session.add(student)
    db.session.commit()
    return render_template('addstudent.html', message="Student Added Successfully...")


    return render_template('addstudent.html')

@app.route('/stud-delete/<int:rno>')
def delete_student(rno):
    student = Student.query.filter_by(roll_no = rno).first()
    db.session.delete(student)
    db.session.commit()
    return render_template('liststudent.html', slist=Student.query.all())


def search_student():
    pass


def update_student():
    pass


@app.route('/stud-list')
def list_student():
    return render_template('liststudent.html',slist = Student.query.all())



