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

# количество исполнителей в каждом жанре
print(connection.execute("""SELECT g.name, COUNT(a.name) FROM genre g
JOIN music_genre mg ON mg.fk_genre_id = g.genre_id
JOIN author a ON a.author_id = mg.fk_author_id
GROUP BY g.name
;""").fetchall())

# количество треков, вошедших в альбомы 2019-2020 годов
print(connection.execute("""SELECT COUNT(s.name) FROM album a
JOIN song s ON s.fk_album_id = a.album_id
WHERE year_release BETWEEN 2019 AND 2020;
""").fetchall())

#средняя продолжительность треков по каждому альбому
print(connection.execute("""SELECT a.name, AVG(duration) FROM album a
JOIN song s ON s.fk_album_id = a.album_id
GROUP BY a.name;
""").fetchall())

#все исполнители, которые не выпустили альбомы в 2020 году
print(connection.execute("""SELECT a.name FROM album al
JOIN mix_album ma ON ma.fk_album_id = al.album_id
JOIN author a ON ma.fk_author_id = a.author_id
WHERE al.year_release != 2020;
""").fetchall())

#названия сборников, в которых присутствует конкретный исполнитель Sting
print(connection.execute("""SELECT DISTINCT col.name FROM collection col
JOIN collection_mix col_m ON col_m.collection_id = col.collection_id
JOIN song s ON col_m.song_id = s.song_id
JOIN album al ON al.album_id = s.fk_album_id
JOIN mix_album mix_a ON mix_a.fk_album_id = al.album_id
JOIN author a ON a.author_id = mix_a.fk_author_id
WHERE a.name = 'Sting';
""").fetchall())

#название альбомов, в которых присутствуют исполнители более 1 жанра
print(connection.execute("""SELECT al.name FROM album al
JOIN mix_album mix_a ON mix_a.fk_album_id = al.album_id
JOIN author a ON a.author_id = mix_a.fk_author_id
JOIN music_genre mg ON mg.fk_author_id = a.author_id
GROUP BY al.name
HAVING COUNT(fk_genre_id) > 1;
""").fetchall())

#наименование треков, которые не входят в сборники
print(connection.execute("""SELECT s.name FROM song s
LEFT JOIN collection_mix cm ON cm.song_id = s.song_id
WHERE cm.collection_id IS NULL;
""").fetchall())

#исполнителя(-ей), написавшего самый короткий по продолжительности трек
print(connection.execute("""SELECT a.name FROM author a
JOIN mix_album ma ON ma.fk_author_id = a.author_id
JOIN album al ON al.album_id = ma.fk_album_id
JOIN song s ON s.fk_album_id = al.album_id
GROUP BY a.name
HAVING MIN(s.duration) = (
SELECT MIN(duration) FROM song)
;
""").fetchall())

#название альбомов, содержащих наименьшее количество треков
print(connection.execute("""SELECT al.name FROM album al
JOIN song s ON s.fk_album_id = al.album_id
GROUP BY al.name
HAVING COUNT(*) = (SELECT COUNT(*) FROM album al JOIN song s ON s.fk_album_id = al.album_id GROUP BY al.name LIMIT 1)
;
""").fetchall())
