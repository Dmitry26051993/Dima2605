# Создать шаблон flask_06_form.html с формой Имя, фамилия, возраст.
# Создать вью /form: при GET запросе отображать форму, при POST запросе
# Выводить данные пользователю с помощью шаблона flask_06_display.html
import csv
import os.path

from flask import Flask, request, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/all/')
def all_users():
    with open('flask_05.csv', 'r') as file:
        csvreader = csv.reader(file)
        rows = [row for row in csvreader]
    return render_template('all.html', users=rows[1:])

@app.route('/', methods=['POST', 'GET'], endpoint='custom_login')
def login():
    if request.method == 'POST':
        user = request.form['name']
        lastname = request.form['lastname']
        age = request.form['age']
        data = request.form
        with open('flask_05.csv', 'a') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow([user, lastname, age])

        result = render_template('form_06_01.html', data_for_template=data)
        return result
    else:
        return render_template('form_06.html')


if __name__ == '__main__':
    if not os.path.exists('flask_05.csv'):
        with open('flask_05.csv', 'w') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(["user", 'lastname', 'age'])
    app.run()