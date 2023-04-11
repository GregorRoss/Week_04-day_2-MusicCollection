from db.run_sql import run_sql
from repositories import artist_repository

from models.album import Album

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

def save(album):
    sql =f"INSERT INTO albums(name, genre, artist_id) VALUES (%s, %s, %s)RETURNING *"
    values = [album.name, album.genre, album.artist.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def select_all():  
    albums = [] 

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist_id = row['artist_id']
        artist = artist_repository.select(artist_id)
        album = Album( row['name'], row['genre'], artist, row['id'])
        albums.append(album)
    return albums 

def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        artist_id = results[0]['artist_id']
        artist = artist_repository.select(artist_id)
        album = Album(result['name'], result['genre'], artist, result['id'])
        return album