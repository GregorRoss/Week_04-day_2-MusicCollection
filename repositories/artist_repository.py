from db.run_sql import run_sql

from models.artist import Artist
from models.album import Album

def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)

def save(artist):
    sql =f"INSERT INTO artists(first_name, last_name) VALUES (%s, %s) RETURNING *"
    values = [artist.first_name, artist.last_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = id
    return artist

def select_all():  
    artists = [] 

    sql = "SELECT * FROM artists"
    results = run_sql(sql)

    for row in results:
        artist = Artist(row['first_name'], row['last_name'], row['id'], )
        artists.append(artist)
    return artists

def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        artist = Artist(result['first_name'], result['last_name'], result['id'])
        return artist
