create table book (id integer primary key autoincrement, title varchar, pages int, author varchar, price float)
alter table book add column release_year int
INSERT INTO book (title, pages, author, price, release_year)
values ('War', 100, 'Alexeev', 10, 2005),
('Evil', 50, 'Stalin', 25, 1995),
('Clean', 115, 'Barisov', 9, 2010),
('World', 95, 'Gay', 20, 2001),
('Cinema', 60, 'Fredman', 15, 2009);
select release_year, title, price from book
select title, release_year, price from book
WHERE release_year= 2010
UPDATE book SET price= 10
WHERE release_year = 2010
DELETE FROM book
WHERE price > 10