import sqlite3

# Improved QnA with keywords
data = [


]


# Insert into database
conn = sqlite3.connect('../db/questions.db')
cursor = conn.cursor()
cursor.executemany('''
    INSERT INTO interview_qna (question, answer, keywords) VALUES (?, ?, ?)
''', data)

conn.commit()
conn.close()

print("✅ Database seeded successfully with improved questions.")
