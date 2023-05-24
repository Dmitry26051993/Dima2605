# Создать класс Book и сессию в файле book.py.
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
class Book:
    def __init__(self, title, pages, author, price, release_year):
        self.title = title
        self.pages = pages
        self.author = author
        self.price = price
        self.release_year = release_year
engine = create_engine('sqlite:///book.db',echo = True)
Session = sessionmaker(bind=engine)
session1 = Session()