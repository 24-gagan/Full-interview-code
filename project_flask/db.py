import sqlite3


def get_conn(app):
    return sqlite3.connect(app.config["DATABASE"])


def init_db(app):
    conn = get_conn(app)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE
        )
    """)
    conn.commit()
    conn.close()


def create_user(app, name, email):
    conn = get_conn(app)
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    conn.close()


def get_user(app, email):
    conn = get_conn(app)
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE email = ?", (email,))
    row = cur.fetchone()
    conn.close()
    return row
