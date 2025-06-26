from utils.speech import speak
from utils.listen import listen
import sqlite3


def add_new_question():
    speak("Please say the question.")
    question = listen()

    speak("Now say the answer.")
    answer = listen()

    speak("Please provide some keywords related to this question for evaluation.")
    keywords = listen()

    conn = sqlite3.connect('db/questions.db')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO interview_qna (question, answer, keywords) VALUES (?, ?, ?)",
        (question, answer, keywords)
    )
    conn.commit()
    conn.close()

    speak("Question, answer, and keywords added successfully!")
