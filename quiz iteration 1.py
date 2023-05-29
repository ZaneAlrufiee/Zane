import random

# Define the questions as a list of tuples, each containing the question, answer choices, and correct answer.
questions = [("Who is the current President of the United States?", ["a. Barack Obama", "b. Donald Trump", "c. Joe Biden", "d. George Bush"], "c"),
             ("Who painted the Mona Lisa?", ["a. Michelangelo", "b. Leonardo da Vinci", "c. Vincent van Gogh", "d. Pablo Picasso"], "b"),
             ("What is the largest planet in our solar system?", ["a. Mars", "b. Venus", "c. Jupiter", "d. Saturn"], "c"),
             ("What is the smallest country in the world?", ["a. Monaco", "b. Vatican City", "c. Liechtenstein", "d. San Marino"], "b"),
             ("Which of the following is not a primary color?", ["a. Red", "b. Blue", "c. Green", "d. Yellow"], "c"),
             ("Who wrote the novel 'To Kill a Mockingbird'?", ["a. Harper Lee", "b. Ernest Hemingway", "c. William Faulkner", "d. F. Scott Fitzgerald"], "a"),
             ("What is the capital of Japan?", ["a. Shanghai", "b. Beijing", "c. Toko", "d. Seoul"], "c"),
             ("What is the chemical symbol for gold?", ["a. Ag", "b. Au", "c. Cu", "d. Fe"], "b"),
             ("What is the highest mountain in Africa?", ["a. Mount Everest", "b. Mount Kilimanjaro", "c. Mount Fuji", "d. Mount McKinley"], "b")]

# Shuffle the questions to be randomized each time.
random.shuffle(questions)

# Define variables to keep track of the number of correct and incorrect answers.
correct = 0
incorrect = 0

# Define a function to ask a question and get a response.
def ask_question(question, choices, answer):
    print(question)
    for choice in choices:
        print(choice)
    response = input("Please enter your response: ").lower()
    if response == answer:
        print("Correct!")
        return True
    elif response == "skip":
        print("Question skipped.")
        return False
    elif response == "retry":
        print("Question retrying...")
        return ask_question(question, choices, answer)
    elif response == "reset":
        print("Quiz resetting...")
        return False
    else:
        print("Incorrect.")
        return False

# Define variables to keep track of the questions that have and haven't been attempted.
not_attempted = questions[:]
attempted = []

# Ask each question until all have been attempted or the quiz is reset.
while not_attempted:
    question = not_attempted.pop(0)
    attempted.append(question)
    if ask_question(question[0], question[1], question[2]):
        correct += 1
    else:
        incorrect += 1
    print()
