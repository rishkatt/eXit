import os
import sys
import time

# ---------- Terminal Helpers ----------

def clear():
    os.system("clear")

def slow_print(text, delay=0.035):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

def normalize(text):
    fillers = {"the", "a", "an", "my", "to", "on"}
    words = text.lower().split()
    filtered = [w for w in words if w not in fillers]
    return " ".join(filtered)

def wait_for_command(valid_commands):
    while True:
        user_input = input("> ").strip()
        normalized = normalize(user_input)

        if normalized in valid_commands:
            return normalized
        else:
            slow_print("That doesn't work.", 0.02)

# ---------- Game Screens ----------

def title_screen():
    clear()
    slow_print("eXit\n", 0.08)
    slow_print("Press ENTER to begin", 0.03)
    input()

# ---------- Paths ----------

def friend_path():
    clear()
    slow_print("Your friend hands you a note.")
    slow_print("What do you do?\n")

    wait_for_command({"read note"})

    clear()
    slow_print("The room is too dark.")
    slow_print("What do you do?\n")

    wait_for_command({"light match"})

    clear()
    slow_print('The note says, "Don\'t leave me here."')
    slow_print("Do you leave your friend or stay?\n")

    wait_for_command({"stay"})

    clear()
    slow_print("You chose to stay.")
    slow_print("The game ends here.")
    input("\nPress ENTER to exit.")
    sys.exit()

def first_room():
    clear()
    slow_print("You're trapped in a dungeon with your friend.")
    slow_print("You see a barrel.")
    slow_print("What do you do?\n")

    action = wait_for_command({
        "move barrel",
        "sit down next friend"
    })

    return action

def second_room():
    clear()
    slow_print("The barrel rolls aside and you find a secret tunnel.")
    slow_print("What do you do?\n")

    wait_for_command({"enter tunnel"})

def third_room():
    clear()
    slow_print("You start to escape but your friend is too weak to go with you.")
    slow_print("They hand you a note.")
    slow_print("What do you do?\n")

    wait_for_command({"read note"})

    clear()
    slow_print("It is too dark to read the note.")
    slow_print("What do you do?\n")

    wait_for_command({"leave"})

    clear()
    slow_print("You crawl through the tunnel and the tunnel leads you to a beach.")
    slow_print("What do you do?\n")

    wait_for_command({"look"})

    clear()
    slow_print("In the water, you see a boat.")
    slow_print("What do you do?\n")

    wait_for_command({"get boat", "get on boat"})

def ending():
    clear()
    slow_print("Congratulations, you're heading to a new world!")
    slow_print("Do you want to play again? (Y/N)\n")

    while True:
        choice = input("> ").strip().lower()
        if choice == "y":
            return True
        elif choice == "n":
            return False
        else:
            slow_print("Please enter Y or N.", 0.02)

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

