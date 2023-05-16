create table user (id integer primary key autoincrement, firstname varchar, lastname varchar, age integer)
INSERT INTO user (firstname, lastname, age)
values ('Dmitry', 'Martynovich', 29),
('Alex', 'Maraimov', 25),
('Denis', 'Kulic', 26),
('Dmitry', 'Kulic', 26),
('Victoria', 'Usovnichenko', 19)
select * from user
WHERE firstname = 'Dmitry'
select * from user
WHERE age < 25
select * from user
WHERE age BETWEEN 19 and 26