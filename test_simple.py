#!/usr/bin/env python3
from pynput import keyboard
import logging
from datetime import datetime

logging.basicConfig(filename='test.log', level=logging.INFO, 
                   format='%(asctime)s - %(message)s')

def on_press(key):
    try:
        print(f"Key pressed: {key}")
        logging.info(f"Key: {key}")
        if key == keyboard.Key.esc:
            return False
    except Exception as e:
        print(f"Error: {e}")

print("Testing... Press ESC to stop")
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
print("Done! Check test.log")