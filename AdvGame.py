def adventure_game():
    print("Welcome to the Adventure!")
    print("You find yourself at a crossroads in a dark forest.\n")

    choice1 = input("Do you go left towards the mountains or right towards the river? (left/right): ").lower()
    
    if choice1 == "left":
        print("\nYou head towards the mountains and find a cave.")
        choice2 = input("Do you enter the cave or keep walking around it? (enter/walk): ").lower()
        
        if choice2 == "enter":
            print("\nInside the cave, you discover a treasure chest full of gold! You win!")
        elif choice2 == "walk":
            print("\nWhile walking around, you encounter a wild bear. You run away safely but find nothing more. The adventure ends.")
        else:
            print("\nInvalid choice. Your adventure ends here.")
    
    elif choice1 == "right":
        print("\nYou walk toward the river and see a boat and a bridge.")
        choice2 = input("Do you take the boat across or cross the bridge? (boat/bridge): ").lower()
        
        if choice2 == "boat":
            print("\nThe boat takes you safely across. On the other side, you find a peaceful village. You are safe. The adventure ends.")
        elif choice2 == "bridge":
            print("\nThe bridge is old and breaks while crossing. You fall into the river but manage to swim to shore. Exhausted, you decide to rest. The adventure ends.")
        else:
            print("\nInvalid choice. Your adventure ends here.")
    
    else:
        print("\nInvalid choice. Your adventure ends here.")

if __name__ == "__main__":
    adventure_game()
