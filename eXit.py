# ---------- Packages -----------
import os
import sys
import time
import platform

# Import if running in Windows
if platform.system() == "Windows":
    import subprocess
    import shutil

# ---------- Terminal Helpers ----------

def clear():
    if platform.system() == "Linux":
        os.system('clear')
    elif platform.system() == "Windows":
        os.system('cls')
    else:
        print("\n" * 100)

def show_image(path):
    system = platform.system()

    # Resolve absolute path safely
    base_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(base_dir, path)

    # ---------- Linux: try imgcat ----------
    if system == "Linux":
        if os.system("command -v imgcat >/dev/null 2>&1") == 0:
            os.system(f"imgcat '{image_path}'")
            return

    # ---------- Windows / fallback: ASCII ----------
    try:
        # Terminal width detection
        try:
            columns = min(os.get_terminal_size().columns, 100)
        except OSError:
            columns = 80

        # Path to binary (adjust if needed)
        converter = os.path.join("bin", "ascii-image-converter.exe")

        if not converter:
            raise RuntimeError("ascii-image-converter not found in PATH")

        cmd = [
            converter,
            image_path,
            "-W", str(columns),
            "--color",
            "--invert"
        ]

        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )

        print(result.stdout)

    except Exception as e:
        print("[Image failed to load]")
        print(f"[DEBUG] {e}")


def normalize(text):
    fillers = {"the", "a", "an", "my", "to", "on"}
    words = text.lower().split()
    filtered = [w for w in words if w not in fillers]
    return " ".join(filtered)

def check_quit(raw_input):
    if raw_input.lower().strip() in {"q", "q()", "exit", "quit"}:
        clear()
        sys.exit()

def wait_for_command(valid_commands, invalid_handlers=None):
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

# ---------- Screens ----------

def title_screen():
    clear()
    show_image("images/exit.png")
    print("Press ENTER to begin")
    input()

def too_dark():
    clear()
    show_image("images/fourth_room_a.png")
    print("It is too dark to read the note.")
    print("What do you do?\n")

# ---------- Paths ----------

def friend_path():
    clear()
    show_image("images/second_room_b.png")
    print("Your friend hands you a note.")
    print("What do you do?\n")

    wait_for_command(
        {"light match"},
        {"read note": too_dark}
    )

    clear()
    show_image("images/third_room_b.png")
    print('The note says, "Don\'t leave me here."')
    print("Do you leave your friend or stay?\n")

    wait_for_command({"stay"})

    clear()
    print("Game terminated.")
    time.sleep(1)
    sys.exit()

def first_room():
    clear()
    show_image("images/first_room.png")
    print("You're trapped in a dungeon with your friend.")
    print("You see a barrel.")
    print("What do you do?\n")

    return wait_for_command({
        "move barrel",
        "sit down next friend"
    })

def second_room():
    clear()
    show_image("images/second_room_a.png")
    print("The barrel rolls aside and you find a secret tunnel.")
    print("What do you do?\n")

    wait_for_command({"enter tunnel"})

def third_room():
    clear()
    show_image("images/third_room_a.png")
    print("You start to escape but your friend is too weak to go with you.")
    print("They hand you a note.")
    print("What do you do?\n")

    wait_for_command(
        {"leave"},
        {"read note": too_dark}
    )

    clear()
    show_image("images/fifth_room_a.png")
    print("You crawl through the tunnel and the tunnel leads you to a beach.")
    print("What do you do?\n")

    wait_for_command({"look"})

    clear()
    show_image("images/sixth_room_a.png")
    print("In the water, you see a boat.")
    print("What do you do?\n")

    wait_for_command({"get boat", "get on boat"})

def ending():
    clear()
    show_image("images/final_room_a.png")
    print("Congratulations, you're heading to a new world!")
    print("Do you want to play again? (Y/N)\n")

    while True:
        choice = input("> ").strip().lower()
        check_quit(choice)
        if choice == "y":
            return True
        if choice == "n":
            return False
        print("Please enter Y or N.")

# ---------- Main ----------

def main():
    while True:
        title_screen()
        path = first_room()

        if path == "sit down next friend":
            friend_path()
        else:
            second_room()
            third_room()
            if not ending():
                clear()
                break

if __name__ == "__main__":
    main()

