# Simple Quiz Game

def ask_question(question, options, correct_answer):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    # Get user's answer
    answer = input("Your answer (1/2/3/4): ").strip()

    # Check if the answer is correct
    if answer.isdigit() and int(answer) == correct_answer:
        print("Correct!\n")
        return True
    else:
        print(f"Wrong! The correct answer was {correct_answer}. {options[correct_answer - 1]}\n")
        return False


def run_quiz(questions):
    score = 0

    # Iterate through the list of questions
    for question, options, correct_answer in questions:
        if ask_question(question, options, correct_answer):
            score += 1

    # Display the final score
    print(f"Quiz completed! Your final score is {score}/{len(questions)}.\n")


# List of questions (question, options, correct_answer)
quiz_questions = [
    ("What is the capital of France?", ["Berlin", "Paris", "Madrid", "Rome"], 2),
    ("Which planet is known as the Red Planet?", ["Earth", "Venus", "Mars", "Jupiter"], 3),
    ("What is the chemical symbol for water?", ["H2O", "O2", "CO2", "H2"], 1),
]

# Run the quiz
run_quiz(quiz_questions)