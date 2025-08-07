import sqlite3

def get_connect():
    con = sqlite3.connect("database/riddles.db")

    con.execute("PRAGMA foreign_keys = ON")

    return con
