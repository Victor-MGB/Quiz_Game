quiz_questions = [
    ("What is the capital of France?", ["A) Berlin", "B) Paris", "C) Rome", "D) Madrid"], "B"),
    ("Which planet is known as the Red Planet?", ["A) Earth", "B) Venus", "C) Mars", "D) Jupiter"], "C"),
    ("What is the largest ocean on Earth?", ["A) Atlantic", "B) Indian", "C) Southern", "D) Pacific"], "D"),
    ("Who wrote 'To Kill a Mockingbird'?", ["A) Harper Lee", "B) J.K. Rowling", "C) Ernest Hemingway", "D) Jane Austen"], "A"),
    ("What is the chemical symbol for water?", ["A) H2O", "B) CO2", "C) NaCl", "D) O2"], "A"),
]

def run_quiz():
    """Function to run the quiz game."""
    score = 0
    
    for question,options,correct_answer in quiz_questions:
        print("\n" + question)
        for option in options:
            print(option)
        user_answer = input("Enter your answer (A,B,C or D) :").upper()
        
        if user_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer was {correct_answer}.")
        
    print(f"\nQuiz completed! Your final score is {score} out of {len(quiz_questions)}.")

if __name__ == "__main__":
    print("Welcome to the Quiz Game")
    run_quiz()
   
