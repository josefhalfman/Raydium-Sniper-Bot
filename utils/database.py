import sqlite3

def init_db():
    print("Initializing database...")
    connection = sqlite3.connect("sniper_bot.db")
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS trades (
        id INTEGER PRIMARY KEY,
        token TEXT NOT NULL,
        price REAL NOT NULL,
        timestamp TEXT NOT NULL
    )""")
    connection.commit()
    connection.close()

def log_trade(token, price, timestamp):
    connection = sqlite3.connect("sniper_bot.db")
    cursor = connection.cursor()
    cursor.execute("INSERT INTO trades (token, price, timestamp) VALUES (?, ?, ?)", (token, price, timestamp))
    connection.commit()
    connection.close()
