# Создать сайт. При запросе на домашнюю страницу отображается текущая дата.
from flask import Flask
from datetime import datetime
app = Flask(__name__)
@app.route('/')
def time():
    return f'Hello, {datetime.now()}'
if __name__ == '__main__':
    app.run()



