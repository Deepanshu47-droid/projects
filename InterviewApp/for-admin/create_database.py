import sqlite3

# Create DB and table
def create_db():
    conn = sqlite3.connect('../db/questions.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS interview_qna (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            answer TEXT NOT NULL,
            keywords TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Call this function once to create the DB
create_db()
