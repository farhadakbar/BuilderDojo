# A quiz game that uses multiple choice

questions = [
    {
        "question": "What is the capital of Bangladesh?",
        "options": ["Chittagong", "Khulna", "Sylhet", "Dhaka"],
        "answer": "D"
    },
    {
        "question": "What is the chemical symbol for the element gold?",
        "options": ["Au", "Ag", "Pb", "Fe"],
        "answer": "A"
    },
    {
        "question": "Which music artist released the best-selling album of all time, Thriller, in 1982?",
        "options": ["Prince", "Michael Jackson", "Madonna", "David Bowie"],
        "answer": "B"
    },
    {
        "question": "What is the capital city of France?",
        "options": ["London", "Berlin", "Paris", "Madrid"],
        "answer": "C"
    },
    {
        "question": "Which of these animals is the tallest in the world?",
        "options": ["Elephant", "Giraffe", "Rhinoceros", "Hippopotamus"],
        "answer": "B"
    },
    {
        "question": "What is the center of our solar system?",
        "options": ["Earth", "Mars", "The Sun", "The Moon"],
        "answer": "C"
    },
    {
        "question": "How many colors are in a standard rainbow?",
        "options": ["5", "6", "7", "8"],
        "answer": "C"
    },
    {
        "question": "Which of these fruits is naturally yellow and curved?",
        "options": ["Apple", "Banana", "Strawberry", "Orange"],
        "answer": "B"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answer": "D"
    },
    {
        "question": "In the classic fairy tale, what wakes Sleeping Beauty from her deep slumber?",
        "options": ["A glass slipper", "A true love's kiss", "A magic potion", "A loud alarm clock"],
        "answer": "B"
    }
]

def display_question(question):
    print(question["question"])
    letters = "ABCD"

    for index, option in enumerate(question["options"]):
        print(f"{letters[index]}. {option}")

def ask_question(question):
    while True:
        answer = input("Enter your answer (A,B, C, or D): ").upper()

        if answer in ["A", "B", "C", "D"]:
            break
        else:
            print("Invalid answer. Please enter A, B, C, or D.")

    if answer == question["answer"]:
        print("Correct!")
        return True
    else:
        print("Incorrect!")
        return False

def play_quiz(questions):
    score = 0

    for question in questions:
        display_question(question)
        if ask_question(question):
            score += 1

    print(f"Final Score: {score}/{len(questions)}")

play_quiz(questions)