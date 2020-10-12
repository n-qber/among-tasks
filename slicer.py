from pynput.keyboard import Listener
from os import listdir
from pyperclip import copy as cp
import os.path

path = r"D:\Games\Among.Us.v2020\Among.Us.v2020\TaskHack\task-prints\general"
files = listdir(path)


def copy():
    global files
    print(files[0])
    cp(os.path.join(path, files[0]))
    files = files[1:]


def on_press(key):
    if hasattr(key, 'vk') and key.vk == 79:
        copy()


with Listener(on_press=on_press) as l:
    l.join()
