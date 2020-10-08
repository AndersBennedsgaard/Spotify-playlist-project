import os
import sqlite3


raise NotImplementedError("Modules not tested")
DATABASE_NAME = 'tracks.db'


def create_track_db():
    if os.path.exists(DATABASE_NAME):
        raise FileExistsError("Database already exist")
    con = sqlite3.connect(DATABASE_NAME)
    cur = con.cursor()
    cur.execute(
        """CREATE TABLE tracks
        (id str unique, name str, features real)
        """
    )
    # TODO: Correct features
    # TODO: Use with commands
    con.commit()
    con.close()


def collect_features_db(track_ids):
    con = sqlite3.connect(DATABASE_NAME)
    # TODO: Test execute command
    with con:
        cur = con.cursor()
        cur.execute(f"SELECT * FROM tracks WHERE id IN ({', '.join(tuple(track_ids))})")
        features = cur.fetchall()
    return features


def append_features_db(track_features):
    con = sqlite3.connect(DATABASE_NAME)
    cur = con.cursor()
    # TODO: Test if id's already in the table can be inserted
    cur.executemany("INSERT INTO tracks VALUES (?, ?, ?)", track_features)
