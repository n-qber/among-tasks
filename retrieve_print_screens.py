from pynput.keyboard import Listener
from PIL import ImageGrab
from os import mkdir, listdir
import os

if "task-prints" not in listdir():
    mkdir("task-prints")


def as_next(files):
    ffiles = []
    for file in files:
        formatted = os.path.splitext(os.path.split(file)[-1])[0]
        if formatted.isnumeric() and file.endswith(".jpg"):
            ffiles += formatted
    if not len(ffiles):
        return "0.jpg"
    return str(int(sorted(ffiles, reverse=True)[0]) + 1) + ".jpg"


def save_image(image):
    already = listdir("task-prints")
    image.save(os.path.join("task-prints", as_next(already)))


def on_press(key):
    if hasattr(key, "char") and key.char == 'p':
        save_image(ImageGrab.grab())


with Listener(on_press=on_press) as l:
    l.join()
