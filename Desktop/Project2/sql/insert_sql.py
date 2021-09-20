import sqlalchemy
import psycopg2

db = 'postgresql://dima:dima@localhost:5432/songs'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

connection.execute("""INSERT INTO author
VALUES
(1, 'Sting'),
(2, 'Вера Брежнева'),
(3, 'Валерий Меладзе'),
(4, 'Вячеслав Бутусов'),
(5, 'Виктор Цой'),
(6, 'Юрий Шевчук'),
(7, 'Митя Фомин'),
(8, 'Жанна Агузарова');
""")
connection.execute("""INSERT INTO genre
VALUES
(1, 'Pop'),
(2, 'Rock'),
(3, 'Chanson'),
(4, 'Country'),
(5, 'Reggae');
""")
connection.execute("""INSERT INTO album
VALUES
(1, 'Brand New Day', 1999),
(2, 'Ververa', 2015),
(3, 'Вопреки', 2008),
(4, 'Goodbuy America', 2007),
(5, 'Звезда по имени Солнце', 1989),
(6, 'Это Все', 1995),
(7, 'Апрель', 2020),
(8, 'Русский Альбом', 1991);
""")
connection.execute("""INSERT INTO mix_album
VALUES
(1,1),
(2,2),
(3,3),
(4,4),
(5,5),
(6,6),
(7,7),
(8,8);
""")
connection.execute("""INSERT INTO song
VALUES
(1, 'Englishman in New York', 210, 1),
(2, 'Сестра', 234, 2),
(3, 'Крылья', 300, 4),
(4, 'Родина', 210, 6),
(5, 'Peace in hands', 220, 3),
(6, 'Перемен!', 290, 5),
(7, 'Все будет хорошо', 250, 7),
(8, 'Странный человек', 270, 8),
(9, 'Восьмиклассница', 190, 5),
(10, 'Shape of my heart', 223, 1),
(11, 'Desert of Rose', 195, 1),
(12, 'Зверь', 260, 4),
(13, 'Roxanne', 250, 1),
(14, 'Это Все', 300, 6),
(15, 'De Do Do', 205, 1);
""")
connection.execute("""INSERT INTO collection
VALUES
(1, 'Russian mix', 2018),
(2, 'Rock mix', 2010),
(3, 'Everything', 2015),
(4, 'Old School', 2020),
(5, 'From Russia with Love', 2012),
(6, 'Pop mix max', 2020),
(7, 'All good', 2015),
(8, 'Sting and Co.', 2021); 
""")
connection.execute("""INSERT INTO collection_mix
VALUES
(1, 2),
(1, 7),
(2, 3),
(2, 4),
(3, 1),
(3, 14),
(3, 15),
(3, 12),
(4, 9),
(4, 14),
(5, 3),
(5, 6),
(5, 4),
(6, 2),
(6, 13),
(6, 7),
(7, 7),
(7, 2),
(7, 10),
(7, 13),
(8, 1),
(8, 3),
(8, 15);
""")

connection.execute("""INSERT INTO music_genre
VALUES
(1, 1),
(1, 2),
(1, 5),
(1, 4),
(2, 1),
(3, 1),
(4, 1),
(4, 2),
(5, 2),
(5, 1),
(6, 1),
(6, 2),
(6, 3),
(7, 1),
(8, 1),
(8, 2),
(8, 3);
""")