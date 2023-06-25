# Создать шаблон flask_06_form.html с формой Имя, фамилия, возраст.
# Создать вью /form: при GET запросе отображать форму, при POST запросе
# Выводить данные пользователю с помощью шаблона flask_06_display.html
import csv
import os.path
from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from flask import Flask, request, render_template

app = Flask(__name__, template_folder='templates')

app = Flask(__name__, template_folder='templates')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flaskschool.db'
db = SQLAlchemy(app)



class Base(db.Model):
    __abstract__ = True

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Group(Base):
    id = db.Column('id', db.Integer, primary_key=True)
    fullname = db.Column(db.String(100))


class Student(Base):
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    group_id = db.Column(db.Integer, ForeignKey(Group.id), nullable=True)
    group = relationship('Group', foreign_keys='Student.group_id', backref='students')


@app.route('/')
def read_group():
    data = Group.query.all()
    return render_template('index.html', groups=data)

@app.route('/read_students/<group_id>')
def read_students(group_id):
    students = Student.query.filter_by(group_id=group_id)
    return render_template('index_students.html', students=students, group_id=group_id)

@app.route('/add', methods=['POST', 'GET'])
def add_group():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        group = Group(fullname=request.form['fullname'])
        group.save()
        return redirect(url_for('read_group'))


@app.route('/add_student', methods=['POST', 'GET'])
def add_student():
    group_id = request.args.get('group_id')
    if request.method == 'GET':
        return render_template('form_student.html', group_id=group_id)
    else:
        student = Student(name=request.form['fullname'], group_id=group_id)
        student.save()
        return redirect(url_for('read_students', group_id=group_id))

@app.route('/update_group', methods=['POST', 'GET'])
def update():
    if request.method == 'GET':
        return render_template('update.html', id=request.args.get('id'))
    else:
        group = db.session.query(Group). \
            filter_by(id=request.args.get('id')).first()
        group.fullname = request.form['fullname']
        group.update()
        return redirect(url_for('read_group'))


@app.route('/delete')
def delete():
    group = Group.query.get(request.args.get('id'))
    group.delete()

    return redirect(url_for('read_group'))


if __name__ == '__main__':
<<<<<<< HEAD
    with app.app_context():
        db.create_all()
    app.run()
=======
    if not os.path.exists('flask_05.csv'):
        with open('flask_05.csv', 'w') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(["user", 'lastname', 'age'])
    app.run()
>>>>>>> b8dca994f7847a654cbadea8449e26344567c216
