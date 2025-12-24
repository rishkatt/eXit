import os
import sys
import time

# ---------- Terminal Helpers ----------

def clear():
    os.system("clear")

def normalize(text):
    fillers = {"the", "a", "an", "my", "to", "on"}
    words = text.lower().split()
    filtered = [w for w in words if w not in fillers]
    return " ".join(filtered)

def check_quit(raw_input):
    quit_commands = {"q", "q()", "exit", "quit"}
    if raw_input.lower().strip() in quit_commands:
        clear()
        sys.exit()

def wait_for_command(valid_commands, invalid_handlers=None):
    """
    valid_commands: set of normalized command strings that advance the game
    invalid_handlers: dict of normalized command -> function to call
    """
    if invalid_handlers is None:
        invalid_handlers = {}

    while True:
        user_input = input("> ").strip()
        check_quit(user_input)

        normalized = normalize(user_input)

        if normalized in invalid_handlers:
            invalid_handlers[normalized]()
            continue

        if normalized in valid_commands:
            return normalized

        print("That doesn't work.")

# ---------- Game Screens ----------

def title_screen():
    clear()
    print("eXit\n")
    print("Press ENTER to begin")
    input()

# ---------- Shared Responses ----------

def too_dark():
    clear()
    print("The room is too dark.")
    print("What do you do?\n")

# ---------- Paths ----------

def friend_path():
    clear()
    print("Your friend hands you a note.")
    print("What do you do?\n")

    wait_for_command(
        valid_commands={"light match"},
        invalid_handlers={
            "read note": too_dark
        }
    )

    clear()
    print('The note says, "Don\'t leave me here."')
    print("Do you leave your friend or stay?\n")

    wait_for_command({"stay"})

    clear()
    print("Game terminated.")
    time.sleep(1)
    sys.exit()

def first_room():
    clear()
    print("You're trapped in a dungeon with your friend.")
    print("You see a barrel.")
    print("What do you do?\n")

    return wait_for_command({
        "move barrel",
        "sit down next friend"
    })

def second_room():
    clear()
    print("The barrel rolls aside and you find a secret tunnel.")
    print("What do you do?\n")

    wait_for_command({"enter tunnel"})

def third_room():
    clear()
    print("You start to escape but your friend is too weak to go with you.")
    print("They hand you a note.")
    print("What do you do?\n")

    wait_for_command(
        valid_commands={"leave"},
        invalid_handlers={
            "read note": too_dark
        }
    )

    clear()
    print("You crawl through the tunnel and the tunnel leads you to a beach.")
    print("What do you do?\n")

    wait_for_command({"look"})

    clear()
    print("In the water, you see a boat.")
    print("What do you do?\n")

    wait_for_command({"get boat", "get on boat"})

def ending():
    clear()
    print("Congratulations, you're heading to a new world!")
    print("Do you want to play again? (Y/N)\n")

    while True:
        choice = input("> ").strip().lower()
        check_quit(choice)

        if choice == "y":
            return True
        elif choice == "n":
            return False
        else:
            print("Please enter Y or N.")

# ---------- Main Loop ----------

def main():
    while True:
        title_screen()
        path = first_room()

        if path == "sit down next friend":
            friend_path()

        elif path == "move barrel":
            second_room()
            third_room()
            if not ending():
                clear()
                break

if __name__ == "__main__":
    main()

