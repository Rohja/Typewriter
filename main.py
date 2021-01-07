#!/usr/bin/env python3

import keyboard
from playsound import playsound
import threading

while True:
    keyboard.wait("enter")
    print("You pressed enter")
    # playsound('sound.mp3')
    threading.Thread(target=playsound, args=('sound.mp3',)).start()
