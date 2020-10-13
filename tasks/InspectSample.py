from Task import Task


class InspectSample(Task):

    def __init__(self):
        self.inspect_button = (1265, 934)
        self.samples_x_positions = range(735, 1190, 113)
        self.samples_y_position = 485
        self.samples_button_y_position = 848
        self.magic_gray_color = 189
        super().__init__()

    def _solve(self, frame):
        pixels = frame.load()

        if pixels[self.inspect_button][0] != self.magic_gray_color:
            self.click(self.inspect_button)
            return True

        for sample_x in self.samples_x_positions:
            if pixels[sample_x, self.samples_y_position][0] > 200:
                self.click(sample_x, self.samples_button_y_position)
                return True




if __name__ == '__main__':
    from time import sleep
    sleep(2)
    inspect_sample = InspectSample()
    inspect_sample.solve()
