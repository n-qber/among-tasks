from .Task import Task


class CleanO2(Task):

    def __init__(self):
        self.top_left = (697, 97)
        self.bottom_right = (1400, 982)

        self.x_difference = 15
        self.y_difference = 15

        super().__init__()

    def identify_leave(self, pixels):
        for y in range(self.top_left[1], self.bottom_right[1], self.y_difference):
            for x in range(self.top_left[0], self.bottom_right[0], self.x_difference):
                pixel = pixels[x, y]
                if pixel[2] < 100 and abs(pixel[0] - 200) < 15:
                    return x, y

    def remove_leave(self, x, y):
        self.set_pos(x, y)
        self.dragTo(0, 540, .15)

    def _solve(self, frame):
        pixels = frame.load()
        leave_xy = self.identify_leave(pixels)

        if not leave_xy:
            return True

        self.remove_leave(*leave_xy)


if __name__ == '__main__':
    from time import sleep
    sleep(2)
    clean_o2 = CleanO2()
    clean_o2.solve()
