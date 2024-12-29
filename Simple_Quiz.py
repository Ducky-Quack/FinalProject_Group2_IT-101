from random import shuffle

# List of questions and answers
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },

    {
        "question": "What is 5 + 7?",
        "choices": ["A. 10", "B. 12", "C. 13", "D. 15"],
        "answer": "B"
    },

    {
        "question": "Who wrote 'Hamlet'?",
        "choices": ["A. Charles Dickens", "B. J.K. Rowling", "C. William Shakespeare", "D. Mark Twain"],
        "answer": "C"
    },

    {
        "question": "What is the largest planet in our solar system?",
        "choices": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "C"
    },

    {
        "question": "What is the chemical symbol for water?",
        "choices": ["A. CO2", "B. O2", "C. H2O", "D. NaCl"],
        "answer": "C"
    },

    {
        "question": "Which element has the atomic number 1?",
        "choices": ["A. Helium", "B. Hydrogen", "C. Oxygen", "D. Carbon"],
        "answer": "B"
    },

    {
        "question": "In which year did World War II end?",
        "choices": ["A. 1945", "B. 1939", "C. 1941", "D. 1950"],
        "answer": "A"
    },

    {
        "question": "What is the square root of 64?",
        "choices": ["A. 6", "B. 7", "C. 8", "D. 9"],
        "answer": "C"
    }
]

shuffle(quiz_questions)
score = 0
question_number = 1

print("Welcome to our simple quiz! Answer by typing A, B, C, or D.\n")

# Asking randomized questions
for current_question in quiz_questions:
    print(f"Question {question_number}: {current_question['question']}")
    for choice in current_question['choices']:
        print(choice)

    question_number += 1
    
    # Only answer from choices
    while True:
        user_answer = input("Your answer: ").strip().upper()
        if user_answer in ["A", "B", "C", "D"]:
            break
        print("Invalid input. Please enter A, B, C or D.")
    
    # Checking answer
    if user_answer == current_question['answer']:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer was {current_question['answer']}.\n")

# Score result
print(f"Quiz over!\nYour score is {score}/{len(quiz_questions)}.")