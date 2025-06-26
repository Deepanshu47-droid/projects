from utils.speech import speak
from utils.listen import listen
import sqlite3


def register_user():
    speak("Please say your desired username.")
    username = listen()
    speak("Please say your password.")
    password = listen()

    conn = sqlite3.connect('db/questions.db')
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        speak("Registration successful!")
    except sqlite3.IntegrityError:
        speak("This username already exists.")

    conn.close()

def login_user():
    conn = sqlite3.connect('db/questions.db')
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL
        )
    """)
    conn.commit()

    speak("Please say your username.")
    username = listen().lower()

    cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()

    if result:
        user_id = result[0]
        speak(f"Welcome back, {username}.")
    else:
        speak(f"No user found with the name {username}. Would you like to register?")
        response = listen().lower()
        if "yes" in response:
            cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
            conn.commit()
            user_id = cursor.lastrowid
            speak(f"User {username} registered successfully.")
        else:
            speak("Okay, exiting the app.")
            conn.close()
            return None

    conn.close()
    return user_id
