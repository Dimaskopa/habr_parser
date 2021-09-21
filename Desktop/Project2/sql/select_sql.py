import sqlalchemy
import psycopg2

db = 'postgresql://dima:dima@localhost:5432/songs'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

print(connection.execute("""SELECT name, year_release FROM album WHERE year_release >= 2018;""").fetchall())
print(connection.execute("""SELECT name, duration FROM song ORDER BY duration DESC;""").fetchmany(2))
print(connection.execute("""SELECT name, duration FROM song WHERE duration >= 210;""").fetchall())
print(connection.execute("""SELECT name, year_release FROM collection WHERE year_release >= 2018
AND year_release <= 2020;""").fetchall())
print(connection.execute("""SELECT name FROM author WHERE name NOT LIKE '%% %%';""").fetchall())
print(connection.execute("""SELECT name FROM song WHERE name LIKE '%%my%%' OR name LIKE '%%мой%%';""").fetchall())
