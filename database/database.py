import sqlite3

con = sqlite3.connect("database/riddles.db")
con.execute("PRAGMA foreign_keys = ON")

cur = con.cursor()

cur.execute(
    """CREATE TABLE users(
        user_id INT PRIMARY KEY,
        email TEXT NULL,
        phone TEXT NULL,
        balance REAL DEFAULT 0.0
    )"""
)

cur.execute(
    """CREATE TABLE riddles(
        id TEXT PRIMARY KEY,
        riddle_name TEXT NOT NULL,
        first INT NULL,
        second INT NULL,
        third INT NULL,
        amount REAL DEFAULT 0.0,
        sub_start TEXT NOT NULL,
        sub_end TEXT NOT NULL,
        start_at TEXT NOT NULL,
        end_at TEXT NOT NULL,
        FOREIGN KEY (first) REFERENCES users(user_id) ON DELETE SET NULL,
        FOREIGN KEY (second) REFERENCES users(user_id) ON DELETE SET NULL,
        FOREIGN KEY (third) REFERENCES users(user_id) ON DELETE SET NULL
    )"""
)

cur.execute(
    """CREATE TABLE subs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        riddle_id TEXT NOT NULL,
        user_id INT NOT NULL, 
        status BOOL DEFAULT FALSE,
        created_at TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
        FOREIGN KEY (riddle_id) REFERENCES riddles(id) ON DELETE CASCADE
    )"""
)

cur.execute(
    """CREATE TABLE logs(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type INT NOT NULL,
        user_id INT NOT NULL,
        content TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE NO ACTION
    )"""
)