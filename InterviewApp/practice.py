from list_questions import list_all_questions
from utils.speech import speak
from utils.listen import listen
import sqlite3


def get_answer(question_text):
    conn = sqlite3.connect('db/questions.db')
    cursor = conn.cursor()
    cursor.execute("SELECT answer FROM interview_qna WHERE question LIKE ?", ('%' + question_text + '%',))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None


def practice_mode():
    speak("Entering practice mode.")

    # First, list all present questions
    questions = list_all_questions()

    if not questions:
        speak("Practice mode cannot start without questions.")
        return

    speak("You can now ask me any question from the list.")
    speak("Say 'stop' anytime to exit practice mode.")

    while True:
        speak("Ask me a question.")
        user_question = listen()

        if "stop" in user_question.lower():
            speak("Exiting practice mode.")
            break

        answer = get_answer(user_question)
        if answer:
            speak(answer)
            print(f"Answer: {answer}")
        else:
            speak("Sorry, I do not have an answer to that question.")
            print("Answer not found.")