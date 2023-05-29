import tkinter as tk
from tkinter import messagebox
import random

class QuizGUI:
    def __init__(self, questions):
        self.questions = questions
        self.current_question = 0
        self.score = 0

        # Create the main window
        self.root = tk.Tk()
        self.root.title("Multiple-Choice Quiz")

        # Create the question label
        self.question_label = tk.Label(self.root, text="")
        self.question_label.pack()

        # Create the radio buttons for choices
        self.radio_var = tk.IntVar()
        self.radio_var.set(-1)

        self.radio_buttons = []
        for i in range(4):
            radio_button = tk.Radiobutton(self.root, variable=self.radio_var, value=i)
            self.radio_buttons.append(radio_button)
            radio_button.pack()

        # Create the Skip and Next buttons
        self.skip_button = tk.Button(self.root, text="Skip", command=self.skip_question)
        self.skip_button.pack(side=tk.LEFT)

        self.next_button = tk.Button(self.root, text="Next", command=self.next_question)
        self.next_button.pack(side=tk.RIGHT)

        # Shuffle the order of questions
        random.shuffle(self.questions)

        # Display the first question
        self.display_question()

    def display_question(self):
        # Get the current question
        question = self.questions[self.current_question]
        # Set the question text
        self.question_label.configure(text=question[0])

        # Set the text for each radio button choice
        for i, choice in enumerate(question[1]):
            self.radio_buttons[i].configure(text=choice)

    def skip_question(self):
        # Move to the next question without increasing the score
        self.current_question += 1

        if self.current_question < len(self.questions):
            # If there are more questions, display the next question
            self.display_question()
        else:
            # If all questions have been answered, show the final score and prompt for restart
            messagebox.showinfo("Quiz Finished", f"Your score: {self.score}/{len(self.questions)}")
            restart = messagebox.askyesno("Quiz Restart", "Do you want to restart the quiz?")
            if restart:
                self.restart_quiz()
            else:
                self.root.destroy()

    def next_question(self):
        # Get the selected choice
        selected_choice = self.radio_var.get()
        if selected_choice == -1:
            # Display an error message if no choice is selected
            messagebox.showerror("Error", "Please select an answer!")
            return

        # Get the current question
        question = self.questions[self.current_question]
        if question[2] == selected_choice:
            # Increase the score if the selected choice is correct
            self.score += 1
            feedback = "Correct!"
        else:
            feedback = "Incorrect!"

        # Move to the next question and reset the radio button selection
        self.current_question += 1
        self.radio_var.set(-1)

        if self.current_question < len(self.questions):
            # If there are more questions, display the next question
            self.display_question()
        else:
            # If all questions have been answered, show the final score and prompt for restart
            messagebox.showinfo("Quiz Finished", f"Your score: {self.score}/{len(self.questions)}")
            restart = messagebox.askyesno("Quiz Restart", "Do you want to restart the quiz?")
            if restart:
                self.restart_quiz()
            else:
                self.root.destroy()

        # Display the feedback for the current question
        messagebox.showinfo("Feedback", feedback)

    def restart_quiz(self):
        # Reset quiz variables and shuffle the questions again
        self.current_question = 0
        self.score = 0
        random.shuffle(self.questions)
        self.display_question()


# Questions
questions = [
    ("Who is the current President of the United States?", ["a. Barack Obama", "b. Donald Trump", "c. Joe Biden", "d. George Bush"], 2),
    ("Who painted the Mona Lisa?", ["a. Michelangelo", "b. Leonardo da Vinci", "c. Vincent van Gogh", "d. Pablo Picasso"], 1),
    ("What is the largest planet in our solar system?", ["a. Mars", "b. Venus", "c. Jupiter", "d. Saturn"], 2),
    ("What is the smallest country in the world?", ["a. Monaco", "b. Vatican City", "c. Liechtenstein", "d. San Marino"], 1),
    ("Which of the following is not a primary color?", ["a. Red", "b. Blue", "c. Green", "d. Yellow"], 2),
    ("Who wrote the novel 'To Kill a Mockingbird'?", ["a. Harper Lee", "b. Ernest Hemingway", "c. William Faulkner", "d. F. Scott Fitzgerald"], 0),
    ("What is the capital of Japan?", ["a. Shanghai", "b. Beijing", "c. Tokyo", "d. Seoul"], 2),
    ("What is the chemical symbol for gold?", ["a. Ag", "b. Au", "c. Cu", "d. Fe"], 1),
    ("What is the highest mountain in Africa?", ["a. Mount Everest", "b. Mount Kilimanjaro", "c. Mount Fuji", "d. Mount McKinley"], 1)
]

# Create the quiz GUI
quiz = QuizGUI(questions)
# Run the main event loop
quiz.root.mainloop()
