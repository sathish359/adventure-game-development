import time

def introduction():
    print("Welcome to the Text-based Adventure Game!")
    print("You find yourself standing at the entrance of a mysterious cave.")
    print("Your choices will determine your fate. Choose wisely!\n")

def make_choice(choices):
    print("Choose your next move:")
    for index, choice in enumerate(choices, start=1):
        print(f"{index}. {choice}")

    while True:
        try:
            choice_index = int(input("Enter the number of your choice: "))
            if 1 <= choice_index <= len(choices):
                return choice_index
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Invalid input. Enter a number.")

def play_game():
    introduction()

    # Initial player information
    player_inventory = []
    player_progress = 0

    # Game loop
    while True:
        if player_progress == 0:
            print("\nYou enter the cave and encounter a fork in the path.")
            choice = make_choice(["Go left", "Go right"])
            if choice == 1:
                print("You chose to go left. A mysterious figure offers you a key.")
                player_inventory.append("Key")
                player_progress = 1
            else:
                print("You chose to go right. You find a hidden passage.")
                player_progress = 2

        elif player_progress == 1:
            print("\nYou continue through the cave with the key in hand.")
            choice = make_choice(["Open the rusty door", "Ignore the door"])
            if choice == 1 and "Key" in player_inventory:
                print("The door creaks open, revealing a treasure room.")
                player_progress = 3
            elif choice == 1:
                print("The door is locked. You need a key.")
            else:
                print("You decide to ignore the door and continue exploring.")
                player_progress = 2

        elif player_progress == 2:
            print("\nYou discover a dark chamber with a sleeping dragon.")
            choice = make_choice(["Attempt to sneak past", "Confront the dragon"])
            if choice == 1:
                print("You successfully sneak past the dragon.")
                player_progress = 3
            else:
                print("The dragon wakes up and breathes fire. Game over!")
                break

        elif player_progress == 3:
            print("\nYou reach the end of the cave and find the exit.")
            choice = make_choice(["Leave the cave", "Search for more treasures"])
            if choice == 1:
                print("Congratulations! You successfully completed the adventure.")
                print("Thank you for playing!")
                break
            else:
                print("You decide to search for more treasures. The adventure continues.")
                player_progress = 4

        elif player_progress == 4:
            print("\nYou venture deeper into the cave and encounter a magical portal.")
            choice = make_choice(["Enter the portal", "Stay in the cave"])
            if choice == 1:
                print("The portal transports you to another world. Game over!")
                break
            else:
                print("You choose to stay in the cave. The adventure continues.")
                player_progress = 3

if __name__ == "__main__":
    play_game()
