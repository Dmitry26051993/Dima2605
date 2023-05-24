from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

engine = create_engine('sqlite:///sa_test.db')
with engine.connect() as connection:
    transaction = connection.begin()
    title = input('title: ')
    pages = int(input('pages: '))
    author = input('author: ')
    price = float(input('price: '))
    releace_year = int(input('releace_year: '))
    try:
        create_table_query = f"""
            insert into Book (title, pages,
                  author, price, release_year)
                  values (:title, :pages, 
                  :author, :price, :releace_year);
        """
        ddl = text(create_table_query).bindparams(
            title=title,
            pages=pages,
            author=author,
            price=price,
            releace_year=releace_year
        )
        connection.execute(ddl)
        choise_trans = input(f'do you want to save book with '
                             f'id={id}, title={title}, pages={pages}, '
                             f'author={author}, price={price},'
                             f' releace_year={releace_year} \n'
                             f'press y to save, something else for no: ')
        if choise_trans in 'yY':
            transaction.commit()
        else:
            transaction.rollback()
    except SQLAlchemyError as e:
        transaction.rollback()