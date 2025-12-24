import os
import sys

def clear():
    os.system("clear")

def title_screen():
    clear()
    print("eXit\n")
    print("Press ENTER to begin")
    input()

def first_room():
    clear()
    print("You're trapped in a dungeon with your friend.")
    print("You see a barrel.")
    print("What do you do?\n")

    while True:
        choice = input("> ").strip().lower()

        if choice == "move the barrel":
            return "barrel"

        elif choice == "sit down next to my friend":
            friend_path()
            sys.exit()  # Exit game after staying

        else:
            print("That doesn't work.")

def friend_path():
    clear()
    print("Your friend hands you a note.")
    print("What do you do?\n")

    while True:
        choice = input("> ").strip().lower()
        if choice == "read note":
            break
        else:
            print("That doesn't work.")

    clear()
    print("The room is too dark.")
    print("What do you do?\n")

    while True:
        choice = input("> ").strip().lower()
        if choice == "light a match":
            break
        else:
            print("That doesn't work.")

    clear()
    print('The note says, "Don\'t leave me here."')
    print("Do you leave your friend or stay?\n")

    while True:
        choice = input("> ").strip().lower()
        if choice == "stay":
            clear()
            print("You chose to stay.")
            print("The game ends here.")
            input("\nPress ENTER to exit.")
            return
        else:
            print("That doesn't work.")

def second_room():
    clear()
    print("The barrel rolls aside and you find a secret tunnel.")
    print("What do you do?\n")

    while True:
        choice = input("> ").strip().lower()
        if choice == "enter the tunnel":
            return
        else:
            print("That doesn't work.")

def third_room():
    clear()
    print("You start to escape but your friend is too weak to go with you.")
    print("They hand you a note.")
    print("What do you do?\n")

    while True:
        choice = input("> ").strip().lower()
        if choice == "read note":
            break
        else:
            print("That doesn't work.")

    clear()
    print("It is too dark to read the note.")
    print("What do you do?\n")

    while True:
        choice = input("> ").strip().lower()
        if choice == "leave":
            break
        else:
            print("That doesn't work.")

    clear()
    print("You crawl through the tunnel and the tunnel leads you to a beach.")
    print("What do you do?\n")

    while True:
        choice = input("> ").strip().lower()
        if choice == "look":
            break
        else:
            print("That doesn't work.")

    clear()
    print("In the water, you see a boat.")
    print("What do you do?\n")

    while True:
        choice = input("> ").strip().lower()
        if choice == "get on the boat":
            break
        else:
            print("That doesn't work.")

def ending():
    clear()
    print("Congratulations, you're heading to a new world!")
    print("Do you want to play again? (Y/N)\n")

    while True:
        choice = input("> ").strip().lower()
        if choice == "y":
            return True
        elif choice == "n":
            return False
        else:
            print("Please enter Y or N.")

def main():
    while True:
        title_screen()
        path = first_room()

        if path == "barrel":
            second_room()
            third_room()
            if not ending():
                clear()
                break

if __name__ == "__main__":
    main()

