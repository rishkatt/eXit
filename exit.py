import os

def clear():
    os.system("clear")

def title_screen():
    clear()
    print("eXit\n")
    print("Press ENTER to begin")
    input()  # Waits for ENTER

def first_room():
    clear()
    print("You're trapped in a dungeon with your friend.")
    print("You see a barrel.")
    print("What do you do?\n")

    while True:
        choice = input("> ").strip()
        if choice.lower() == "move the barrel":
            return
        else:
            print("That doesn't work.")

def second_room():
    clear()
    print("The barrel rolls aside and you find a secret tunnel.")
    print("What do you do?\n")

def main():
    title_screen()
    first_room()
    second_room()

if __name__ == "__main__":
    main()

