import pyautogui
from PIL import ImageGrab


class Task:

    @staticmethod
    def set_pos(x, y, *args, **kwargs):
        pyautogui.moveTo(x, y, *args, **kwargs)

    @staticmethod
    def move(x, y, *args, **kwargs):
        pyautogui.move(x, y, *args, **kwargs)

    @staticmethod
    def actual_pos():
        return pyautogui.position()

    @staticmethod
    def dragTo(x, y, duration=0.0, **kwargs):
        pyautogui.dragTo(x, y, duration, **kwargs)

    @staticmethod
    def click(x=None, y=None, clicks=1):
        pyautogui.click(x=x, y=y, clicks=clicks)

    @staticmethod
    def click_up():
        pyautogui.mouseUp()

    @staticmethod
    def click_down():
        pyautogui.mouseDown()

    @staticmethod
    def sleep(seconds):
        pyautogui.sleep(seconds)

    def _solve(self, frame):
        pass

    def solve(self):
        while True:
            frame = ImageGrab.grab()
            if self._solve(frame):
                return
