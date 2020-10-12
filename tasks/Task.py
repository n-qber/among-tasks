from pynput.mouse import Controller, Button
from PIL import ImageGrab
from time import sleep


class Task:
    def __init__(self):
        self.mouse = Controller()

    def set_pos(self, posX, posY):
        posX_original, posY_original = list(self.mouse.position)
        self.mouse.move(posX - posX_original, posY - posY_original)

    def drag(self, posX, posY, cooldown=.05):
        posX_original, posY_original = list(self.mouse.position)

    def click(self, times=1):
        self.mouse.click(Button.left, times)

    def click_down(self):
        self.mouse.press(Button.left)

    def click_up(self):
        self.mouse.release(Button.left)

    def sleep(self, time):
        sleep(time)

    def _solve(self, frame):
        pass

    def solve(self):
        while True:
            frame = ImageGrab.grab()
            if self._solve(frame):
                return
