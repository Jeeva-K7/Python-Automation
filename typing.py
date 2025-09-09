import pyautogui
import keyboard
import time
import threading
import random

typing = False

def type_i_pattern():
    global typing
    while typing:
        count = random.randint(6, 15)  # Random count of 'i's
        pyautogui.write('i' * count)
        time.sleep(0.1)
        pyautogui.press('backspace', presses=(count - 1), interval=0.05)  # Keep first 'i'
        time.sleep(0.3)

def main():
    global typing
    print("Script started. Type 'jeeva1005' to start. Press ESC to stop.")

    buffer = ""

    while True:
        event = keyboard.read_event()

        if event.event_type == keyboard.KEY_DOWN:
            key = event.name

            # Ignore modifier keys
            if len(key) > 1 and key != 'esc':
                continue

            buffer += key.lower()

            if buffer.endswith("jeeva1005"):
                print("Trigger detected: Starting pattern.")
                typing = True
                threading.Thread(target=type_i_pattern, daemon=True).start()
                buffer = ""

            elif key == "esc":
                typing = False
                print("Typing stopped.")
                buffer = ""

            if len(buffer) > 12:
                buffer = buffer[-12:]

if __name__ == "__main__":
    main()
