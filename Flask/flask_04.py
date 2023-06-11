# Создать шаблон с формой Имя, фамилия, возраст.
# Передать данные на вью дописать эти данные в файл
import os
import csv
from flask import Flask, request

app = Flask(__name__)


@app.route('/users', methods=['POST', 'GET'])
def add_user():
    if request.method == 'GET':
        return """<form action="http://localhost:5000/users" method="post">
    <p>Enter firstname:</p>
    <input type="text" name="firstname"><br>
    <p>Enter lastname:</p>
    <input type="text" name="lastname"><br>
    <p>Enter age:</p>
    <input type="number" name="age"><br>
    <input type="submit">"""
    else:
        user = list(request.form.values())
        with open('dop_04.csv', 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(user)
        return f"""user {user[0]} {user[1]} {user[2]} added to file
    <form action="http://localhost:5000/users" method="get">
    <p>if you want to add new user </p>
    <input type="submit" value="press this button">"""


if __name__ == '__main__':
    if not os.path.exists('dop_04.csv'):
        with open('dop_04.csv', 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            fields = ['first name', 'last name', 'age']
            csvwriter.writerow(fields)
    app.run()