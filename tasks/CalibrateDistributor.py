from Task import Task


class CalibrateDistributor(Task):

    def __init__(self):
        self.y_buttons_range = [230, 500, 770]
        self.x_distributor_view = 1230
        self.distributor_index = 0
        self.supplement = 80
        super().__init__()

    def _solve(self, frame):
        pixels = frame.load()

        if pixels[self.x_distributor_view, self.y_buttons_range[self.distributor_index]] != (0, 0, 0):
            self.click(self.x_distributor_view, self.y_buttons_range[self.distributor_index] + self.supplement)
            self.distributor_index += 1

        return self.distributor_index == 3


if __name__ == '__main__':
    from time import sleep
    sleep(2)
    calibrate_distributor = CalibrateDistributor()
    calibrate_distributor.solve()
