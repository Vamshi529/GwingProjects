import random

def rock_paper_scissors():
    choices = ['rock', 'paper', 'scissors']
    user_wins = 0
    comp_wins = 0
    
    print("Let's play Rock, Paper, Scissors!")
    print("Type 'quit' to stop playing.\n")
    
    while True:
        user_choice = input("Enter rock, paper, or scissors: ").lower()
        if user_choice == 'quit':
            break
        if user_choice not in choices:
            print("Invalid choice, try again.")
            continue
        
        comp_choice = random.choice(choices)
        print(f"Computer chose: {comp_choice}")
        
        if user_choice == comp_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and comp_choice == 'scissors') or \
             (user_choice == 'paper' and comp_choice == 'rock') or \
             (user_choice == 'scissors' and comp_choice == 'paper'):
            print("You win this round!")
            user_wins += 1
        else:
            print("Computer wins this round!")
            comp_wins += 1
        
        print(f"Score -> You: {user_wins} | Computer: {comp_wins}\n")
    
    print("Thanks for playing!")
    print(f"Final Score -> You: {user_wins} | Computer: {comp_wins}")

if __name__ == "__main__":
    rock_paper_scissors()
