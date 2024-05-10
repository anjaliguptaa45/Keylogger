Here's a breakdown of how it works:

We import Key and Listener from the pynput.keyboard module. Key represents the keys being pressed, and Listener is used to listen for keyboard events.
We define the path to the log file where we'll store the keystrokes.
The on_press function is called whenever a key is pressed. It writes the pressed key to the log file.
The on_release function is called when a key is released. We're using it to check if the "Escape" key is pressed, and if so, we stop the listener.
We start the listener with the Listener context manager, specifying the on_press and on_release functions. The listener will run until the "Escape" key is pressed.
To run this code:

Make sure you have Python installed on your system.
Install the pynput library by running pip install pynput in your terminal or command prompt.
Save the code in a Python file (e.g., keylogger.py).
Run the Python file (python keylogger.py).
