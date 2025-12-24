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

def wait_for_command(valid_commands):
    while True:
        user_input = input("> ").strip()
        normalized = normalize(user_input)

        if normalized in valid_commands:
            return normalized
        else:
            print("That doesn't work.")

# ---------- Game Screens ----------

def title_screen():
    clear()
    print("eXit\n")
    print("Press ENTER to begin")
    input()

# ---------- Paths ----------

def friend_path():
    clear()
    print("Your friend hands you a note.")
    print("What do you do?\n")

    wait_for_command({"read note"})

    clear()
    print("The room is too dark.")
    print("What do you do?\n")

    wait_for_command({"light match"})

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

    action = wait_for_command({
        "move barrel",
        "sit down next friend"
    })

    return action

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

    wait_for_command({"read note"})

    clear()
    print("It is too dark to read the note.")
    print("What do you do?\n")

    wait_for_command({"leave"})

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
    print("Congratulations, you're heading to a new wo

