#Quize game

questions = [

    {
        "question": "What is the capital of India?",
        "options": [
            "Mumbai",
            "Delhi",
            "Chennai",
            "Kolkata"
        ],
        "answer": 2
    },

    {
        "question": "Which keyword is used to create a function in Python?",
        "options": [
            "function",
            "define",
            "def",
            "create"
        ],
        "answer": 3
    },

    {
        "question": "Which data type stores key-value pairs?",
        "options": [
            "List",
            "Tuple",
            "Dictionary",
            "Set"
        ],
        "answer": 3
    },

    {
        "question": "Which loop runs until a condition becomes False?",
        "options": [
            "for",
            "while",
            "if",
            "switch"
        ],
        "answer": 2
    },

    {
        "question": "Which symbol is used for comments in Python?",
        "options": [
            "//",
            "#",
            "/* */",
            "--"
        ],
        "answer": 2
    }

]

score = 0
print("\n========== PYTHON QUIZ ==========\n")

for question in questions:
    print(question["question"])

    option_number = 1

    for option in question["options"]:
        print(f"{option_number}. {option}")
        option_number += 1

    user_answer = int(input("Enter your answer: "))

    if user_answer == question["answer"]:
        print("✅ Correct!\n")
        score += 1

    else:
        print("❌ Wrong!")
        print(f"Correct Answer: {question['answer']}\n")

print("========== QUIZ FINISHED ==========")
print(f"Your Score: {score}/{len(questions)}")

