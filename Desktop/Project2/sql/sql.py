import sqlalchemy
import psycopg2

db = 'postgresql://dima:dima@localhost:5432/songs'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

connection.execute("""CREATE table author
(author_id serial PRIMARY KEY,
name text NOT NULL);
""")
connection.execute("""CREATE table genre
(genre_id serial PRIMARY KEY,
name varchar(50));
""")
connection.execute("""CREATE table music_genre
(fk_author_id int REFERENCES author(author_id),
fr_genre_id int REFERENCES genre(genre_id));
""")
connection.execute("""create table album
(album_id serial PRIMARY KEY,
name text NOT NULL,
year_release int CHECK(year_release >= 1500 and year_release <= 2030));
""")
connection.execute("""create table mix_album
(fk_author_id int REFERENCES author(author_id),
fk_album_id int REFERENCES album(album_id));
""")
connection.execute("""create table song
(song_id serial PRIMARY KEY,
name text NOT NULL,
duration int CHECK(duration > 10 and duration < 3600),
fk_album_id int REFERENCES album(album_id));
""")
connection.execute("""create table collection
(collection_id serial PRIMARY KEY,
name text NOT NULL,
year_release int CHECK(year_release >= 1500 and year_release <= 2030));
""")
connection.execute("""create table collection_mix
(collection_id int REFERENCES collection(collection_id),
song_id int REFERENCES song(song_id));
""")