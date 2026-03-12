import sqlite3

# create database connection
def create_connection():
    conn = sqlite3.connect("tickets.db")
    return conn

# create tickets table
def create_table():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tickets (
        ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,
        machine_id TEXT,
        issue TEXT,
        priority TEXT,
        status TEXT
    )
    """)

    conn.commit()
    conn.close()

create_table()