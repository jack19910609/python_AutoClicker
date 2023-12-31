import time
import threading
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Listener, KeyCode, Key ,Controller as KeyboardController


mouseDelay = 0.2
keyboardDelay = 0.01
button = Button.left
start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')


class ClickMouseAndEnter(threading.Thread):
    def __init__(self, mouseDelay,keyboardDelay, button):
        super(ClickMouseAndEnter, self).__init__()
        self.mouseDelay = mouseDelay
        self.keyboardDelay = keyboardDelay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.mouseDelay)
                keyboard.press(Key.enter)
                keyboard.release(Key.enter)
                time.sleep(self.keyboardDelay)
            time.sleep(0.01)

mouse = MouseController()
keyboard = KeyboardController()

click_thread = ClickMouseAndEnter(mouseDelay,keyboardDelay, button)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
