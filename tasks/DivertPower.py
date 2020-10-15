from Task import Task


class DivertPower(Task):

    def __init__(self):
        self.divert_start = 620
        self.divert_compliment = 97
        self.y_pos = 787
        self.drag_to_y = 680
        self.slides = 8
        super().__init__()

    def identify_right_power(self, frame):
        index = 0
        last_r = 0
        for power in range(self.slides):
            r = frame.getpixel((self.divert_start + self.divert_compliment * power, self.y_pos))[0]
            if r > last_r:
                last_r = r
                index = power
        return index

    def drag_by_index(self, index):
        x_pos = self.divert_start + self.divert_compliment * index
        self.set_pos(x_pos, self.y_pos)
        self.click_down()
        self.set_pos(x_pos, self.drag_to_y)
        self.click_up()

    def _solve(self, frame):
        index = self.identify_right_power(frame)
        self.drag_by_index(index)
        return True


if __name__ == '__main__':
    from time import sleep
    sleep(2)
    divert_power = DivertPower()
    divert_power.solve()

