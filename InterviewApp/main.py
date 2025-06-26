from utils.auth import login_user
from add_question import add_new_question
from interview import full_interview
from practice import practice_mode
from utils.speech import speak
from utils.listen import listen
from list_questions import list_all_questions


def main():
    speak("Welcome to the Interview Practice App.")

    # User login before starting
    user_id = login_user()

    if not user_id:
        speak("Login failed. Exiting the app.")
        return

    speak("Say 'add question', 'start interview', 'practice', or 'list questions'.")
    command = listen().lower()

    if "add question" in command:
        add_new_question()
    elif "start interview" in command:
        full_interview(user_id)  # Pass user_id here
    elif "practice" in command:
        practice_mode()
    elif "list questions" in command:
        list_all_questions()
    else:
        speak("Sorry, I didn't understand that.")


if __name__ == "__main__":
    main()
