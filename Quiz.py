def quiz_game():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A) London", "B) Berlin", "C) Paris", "D) Madrid"],
            "answer": "C"
        },
        {
            "question": "Who wrote 'Hamlet'?",
            "options": ["A) Charles Dickens", "B) William Shakespeare", "C) Mark Twain", "D) Leo Tolstoy"],
            "answer": "B"
        },
        {
            "question": "What is the smallest prime number?",
            "options": ["A) 1", "B) 2", "C) 3", "D) 5"],
            "answer": "B"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A) Earth", "B) Venus", "C) Mars", "D) Jupiter"],
            "answer": "C"
        },
        {
            "question": "What is the boiling point of water at sea level (°C)?",
            "options": ["A) 90", "B) 100", "C) 110", "D) 120"],
            "answer": "B"
        }
    ]

    score = 0

    print("Welcome to the Quiz Game!\n")
    
    for i, q in enumerate(questions, 1):
        print(f"Q{i}: {q['question']}")
        for option in q["options"]:
            print(option)
        
        while True:
            answer = input("Your answer (A, B, C, or D): ").strip().upper()
            if answer in ["A", "B", "C", "D"]:
                break
            else:
                print("Invalid input. Please enter A, B, C, or D.")
        
        if answer == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was {q['answer']}.\n")
    
    print(f"Quiz finished! Your final score is {score} out of {len(questions)}.")

if __name__ == "__main__":
    quiz_game()
