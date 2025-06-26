import sqlite3


def create_tables():
    conn = sqlite3.connect('../db/questions.db')
    cursor = conn.cursor()

    # Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    # Interview history table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS interview_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            score REAL NOT NULL,
            date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    ''')

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_tables()
    print("Database tables created successfully!")
