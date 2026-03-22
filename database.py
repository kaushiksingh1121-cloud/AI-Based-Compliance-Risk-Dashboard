import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("compliance.db", check_same_thread=False)
        self.create_table()

    def create_table(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS reports (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                message TEXT,
                risk TEXT,
                score INTEGER
            )
        """)
        self.conn.commit()

    def insert_report(self, message, risk, score):
        self.conn.execute(
            "INSERT INTO reports (message, risk, score) VALUES (?, ?, ?)",
            (message, risk, score)
        )
        self.conn.commit()

    def fetch_reports(self):
        return self.conn.execute("SELECT * FROM reports").fetchall()
