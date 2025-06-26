from utils.speech import speak
from utils.listen import listen
import sqlite3
from datetime import datetime
import time


def evaluate_answer(user_answer, expected_keywords):
    score = 0
    total_keywords = len(expected_keywords)

    for keyword in expected_keywords:
        if keyword.lower() in user_answer.lower():
            score += 1

    if total_keywords == 0:
        return 0

    percentage = (score / total_keywords) * 100
    return round(percentage, 2)


def give_feedback(average_score):
    if average_score >= 85:
        return "Excellent performance! You are well-prepared for your interview."
    elif average_score >= 70:
        return "Good job! You have a solid understanding, but there's room for improvement."
    elif average_score >= 50:
        return "Average performance. Try to include more details in your answers."
    else:
        return "Needs improvement. Focus on key concepts and practice answering confidently."


def save_interview(transcript, average_score, feedback):
    filename = f"recordings/Interview_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, 'w', encoding='utf-8') as file:
        file.write("Interview Transcript\n")
        file.write("-------------------------------\n")
        for entry in transcript:
            file.write(f"Question: {entry['question']}\n")
            file.write(f"Your Answer: {entry['answer']}\n")
            file.write(f"Score: {entry['score']}%\n")
            file.write("-------------------------------\n")
        file.write(f"\nFinal Score: {average_score}%\n")
        file.write(f"Feedback: {feedback}\n")

    print(f"\nInterview transcript saved as {filename}")
    speak(f"Your interview transcript has been saved successfully.")


def save_interview_score(user_id, score):
    conn = sqlite3.connect('db/questions.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO interview_history (user_id, score) VALUES (?, ?)", (user_id, score))
    conn.commit()
    conn.close()


def full_interview(user_id):
    conn = sqlite3.connect('db/questions.db')
    cursor = conn.cursor()

    cursor.execute("SELECT question, keywords FROM interview_qna ORDER BY RANDOM() LIMIT 20")
    questions = cursor.fetchall()
    conn.close()

    total_score = 0
    total_questions = len(questions)
    transcript = []

    speak("Welcome to your interview. I will ask you multiple questions. Please answer after each question.")
    print("\n------ Interview Started ------\n")

    for i, (question, keywords) in enumerate(questions, 1):
        speak(f"Question {i}: {question}")
        print(f"Question {i}: {question}")

        user_answer = listen()

        if keywords:
            keyword_list = [k.strip() for k in keywords.split(',')]
        else:
            keyword_list = []

        score = evaluate_answer(user_answer, keyword_list)
        total_score += score

        print(f"Your score for this question: {score}%")
        speak(f"You scored {score} percent on this question.")

        transcript.append({
            'question': question,
            'answer': user_answer,
            'score': score
        })

        print("-----------------------------")
        time.sleep(1)

    average_score = total_score / total_questions
    feedback = give_feedback(average_score)

    print(f"\n------ Interview Completed ------")
    print(f"Your overall interview score: {average_score}%")
    print(f"Feedback: {feedback}")

    speak(f"Your interview is complete. Your overall score is {average_score} percent.")
    speak(feedback)

    save_interview(transcript, average_score, feedback)
    save_interview_score(user_id, average_score)
