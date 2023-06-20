# Создать папку templates в корне проекта.
# Создать шаблон flask_05.html с формой Имя, фамилия, возраст.
# Создать вью /form: при GET запросе отображать форму,
# при POST запросе дописывать переданные данные в файл.
import csv
import os.path

from flask import Flask, request, render_template

app = Flask(__name__, template_folder='templates')


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

        result = render_template('form_05_01.html', data_for_template=data)
        return result
    else:
        return render_template('form_05.html')


if __name__ == '__main__':
    if not os.path.exists('flask_05.csv'):
        with open('flask_05.csv', 'w') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(["user", 'lastname', 'age'])
    app.run()
