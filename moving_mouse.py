from pynput.keyboard import Listener, Key
from pyautogui import move

commands = {
    Key.up: lambda: move(0, -1),
    Key.down: lambda: move(0, 1),
    Key.left: lambda: move(-1, 0),
    Key.right: lambda: move(1, 0),
}


def on_press(key):
    lm = commands.get(key)
    if lm is not None:
        lm()

with Listener(on_press=on_press) as l:
    l.join()