from utils.speech import speak
from utils.listen import listen
import sqlite3

def add_keywords_to_question():
    conn = sqlite3.connect('db/questions.db')
    cursor = conn.cursor()

    # Step 1: Get question ID or part of the question
    speak("Please say the ID of the question you want to update.")
    question_id = listen()

    try:
        question_id = int(question_id)
    except ValueError:
        speak("Invalid ID. Please provide a valid number.")
        return

    # Step 2: Confirm the question exists
    cursor.execute("SELECT question, keywords FROM interview_qna WHERE id = ?", (question_id,))
    result = cursor.fetchone()

    if result:
        question_text, existing_keywords = result
        speak(f"Found the question: {question_text}")
        if existing_keywords:
            speak(f"Existing keywords are: {existing_keywords}")
        else:
            speak("No keywords are currently set.")

        # Step 3: Get new keywords
        speak("Please say the new keywords you want to add, separated by commas.")
        new_keywords = listen()

        # Step 4: Merge keywords
        if existing_keywords:
            updated_keywords = existing_keywords + ", " + new_keywords
        else:
            updated_keywords = new_keywords

        # Step 5: Update the database
        cursor.execute("UPDATE interview_qna SET keywords = ? WHERE id = ?", (updated_keywords, question_id))
        conn.commit()
        speak("Keywords updated successfully!")

    else:
        speak("No question found with that ID.")

    conn.close()


add_keywords_to_question();