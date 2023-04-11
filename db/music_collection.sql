DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS artists;

CREATE TABLE artists (
  id serial PRIMARY KEY,
  first_name VARCHAR(255),
  last_name VARCHAR(255)
);

CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  genre VARCHAR(255),
  artist_id INT NOT NULL REFERENCES artists(id)
);