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

# ---

