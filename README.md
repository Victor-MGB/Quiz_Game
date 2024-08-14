# Quiz_Game
Project: Quiz Game
Objective:
Develop a simple quiz game where users can answer multiple-choice questions. The game will store questions, options, and correct answers using Python's data structures like tuples or lists. At the end of the quiz, the user's score will be evaluated and displayed.

Components of the Quiz Game
Questions and Answers: A list of tuples will store the questions, possible options, and the correct answer.
User Interaction: Functions to display questions to the user, take input for answers, and provide feedback.
Score Calculation: Track the number of correct answers and display the final score.

Explanation of the Code
Quiz Questions List:

Each tuple contains a question, a list of multiple-choice options, and the correct answer's letter.


Project: Quiz Game
Objective:
Develop a simple quiz game where users can answer multiple-choice questions. The game will store questions, options, and correct answers using Python's data structures like tuples or lists. At the end of the quiz, the user's score will be evaluated and displayed.

Components of the Quiz Game
Questions and Answers: A list of tuples will store the questions, possible options, and the correct answer.
User Interaction: Functions to display questions to the user, take input for answers, and provide feedback.
Score Calculation: Track the number of correct answers and display the final score.
Code Implementation
python
Copy code
# Step 1: Define the quiz questions, options, and answers using a list of tuples
quiz_questions = [
    ("What is the capital of France?", ["A) Berlin", "B) Paris", "C) Rome", "D) Madrid"], "B"),
    ("Which planet is known as the Red Planet?", ["A) Earth", "B) Venus", "C) Mars", "D) Jupiter"], "C"),
    ("What is the largest ocean on Earth?", ["A) Atlantic", "B) Indian", "C) Southern", "D) Pacific"], "D"),
    ("Who wrote 'To Kill a Mockingbird'?", ["A) Harper Lee", "B) J.K. Rowling", "C) Ernest Hemingway", "D) Jane Austen"], "A"),
    ("What is the chemical symbol for water?", ["A) H2O", "B) CO2", "C) NaCl", "D) O2"], "A"),
]

def run_quiz():
    """Function to run the quiz game."""
    score = 0  # Initialize the user's score
    
    # Step 2: Loop through each question and present it to the user
    for question, options, correct_answer in quiz_questions:
        print("\n" + question)
        for option in options:
            print(option)
        
        # Step 3: Get the user's answer
        user_answer = input("Enter your answer (A, B, C, or D): ").upper()
        
        # Step 4: Check if the answer is correct and update the score
        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {correct_answer}.")
    
    # Step 5: Display the final score
    print(f"\nQuiz completed! Your final score is {score} out of {len(quiz_questions)}.")

if __name__ == "__main__":
    print("Welcome to the Quiz Game!")
    run_quiz()
Explanation of the Code
Quiz Questions List:

Each tuple contains a question, a list of multiple-choice options, and the correct answer's letter.
Example:
python
Copy code
("What is the capital of France?", ["A) Berlin", "B) Paris", "C) Rome", "D) Madrid"], "B")
run_quiz() Function:

Score Tracking: Initializes a score variable to keep track of correct answers.
Looping Through Questions: Iterates over each question tuple, displaying the question and options.
User Input: Prompts the user to enter an answer and checks if it matches the correct answer.
Feedback: Provides immediate feedback on whether the answer is correct or wrong, and updates the score accordingly.
Final Score: After all questions are answered, the user's final score is displayed.
Main Execution:

The run_quiz() function is executed only if the script is run directly, ensuring that the quiz starts when the program is run.
Key Concepts and Techniques
Tuples: Used to store fixed data sets like quiz questions, options, and correct answers.
Lists: Employed to manage the multiple-choice options for each question.
Control Flow: Loops and conditionals are used to navigate through the questions and evaluate user responses.
Input and Output: Utilized to interact with the user and display the quiz results.
How to Expand the Project
Randomize Question Order: Use Python’s random.shuffle() to randomize the order of questions for each playthrough.
Add More Questions: Increase the complexity by adding more questions, and maybe even multiple categories.
Track High Scores: Implement a high score feature that stores and displays the top scores.git init
