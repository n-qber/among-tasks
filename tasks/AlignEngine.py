from . import Task
from PIL import Image


class AlignEngine(Task):

    def __init__(self):
        self.width_max = 1320
        self.height_range = 150, 930
        self.aligner_color = (202, 202, 216)
        super().__init__()

    #I spent my day trying to figure out this equation pls be gentle
    @staticmethod
    def calculate_x(y):
        y -= 150
        return (13/25350) * y**2 - 0.4 * y

    def drag_aligner(self, x, y):
        self.set_pos(x, y)
        self.click_down()
        self.set_pos(0, 540)
        self.click_up()

    def _solve(self, frame):
        pixels = frame.load()
        aligner_position = None
        for y in range(*self.height_range):
            x = AlignEngine.calculate_x(y)
            xy = 1320 + int(x), int(y)
            if abs(sum(pixels[xy]) - sum(self.aligner_color)) < 15:
                aligner_position = xy
                break

        if not aligner_position:
            return False

        self.drag_aligner(*aligner_position)

        return True


if __name__ == '__main__':
    from time import sleep
    sleep(2)
    align_engine = AlignEngine()
    align_engine.solve()
