import sys
import random
def introduction():
    print("Welcome to the Mysterious House!")
    print("You are standing in a dimly lit entrance. There are three doors ahead.")

def dark_hallway():
    print("\nYou enter a dark hailway.")
    print("There's a flickering candle and two more door.")
    print("1.Open the first door.")
    print("2.Open the second door.")
    print("3.Go back to the the entrance.")
    
    choice = input("What will you do?")
    
    if choice == "1":
        outcome = random.choice(["You find a hidden treasure!", "A ghost scares you away.", "It's a trap! You fall into a pit."])
        print(outcome)
    elif choice == "2":
        print("You discover a secret passage.")
    elif choice == "3":
        print("You return to the entrance.")
    else:
        print("Invalid choice. Try again.")
        dark_hallway()
    
def dusty_library():
    print("\nYou enter a dusty library.")
    print("There's an old book and a locked chest.")
    print("1. Read the old book.")
    print("2. Try to open the locked chest.")
    print("3. Go back to the entrance.")
    
    choice = input("What will you do?")
    
    if choice == "1":
        print("The book contains ancient spells.")
    elif choice == "2":
        outcome = random.choice(["you find a key inside!", "A trap activates, and you get hurt.", "The chest is empty."])
        print(outcome)
    elif == "3":
        print("You return to the entrance.")
    else:
        print("Invalid choice. Try again.")
        dusty_library()

def creaky_attic():
    print("\nYou climb up to the creaky attic.")
    print("There's a mysterious object covered in a cloth.")
    print("1. Uncover the object.")
    print("2. Leave the attic and go back to the entrance.")
    
    choice = input("What will you do?")
    
    if choice == "1":
        print("You uncover a magical amulet.")
    elif choice == "2":
        print("You descend back to the entrance.")
    else:
        print("Invalid choice. Try again.")
        creaky_attic()
    
def main():
    introduction()
    while True:
        print("\nChoose a room:")
        print("1. Dark Hallway")
        print("2. Dusty Library")
        print("3. Creaky Attic")
        print("4. Quit")
        
        choice = input("Enter the room number or '4' to quit: ")
        
        if choice == "1":
            dark_hallway()
        elif choice == "2":
            dusty_library()
        elif choice == "3":
            creaky_attic()
        elif choice == "4":
            print("Thanks for playing! Goodbye.")
            sys.exit()
        else:
            print("Invalid choice. Try again.")
    
if __name__ == "__main__":
    main()
