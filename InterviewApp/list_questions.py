import sqlite3
from utils.speech import speak


def list_all_questions():
    conn = sqlite3.connect('db/questions.db')
    cursor = conn.cursor()

    cursor.execute("SELECT question, answer FROM interview_qna")
    records = cursor.fetchall()
    conn.close()

    if not records:
        speak("No questions found in the database.")
        print("No questions found.")
        return

    speak(f"There are {len(records)} questions in the database. Reading them now.")
    print(f"\nTotal Questions: {len(records)}\n")

    for i, (question, answer) in enumerate(records, 1):
        print(f"Q{i}: {question}")
        print(f"A{i}: {answer}\n")

    speak("All questions have been listed.")
