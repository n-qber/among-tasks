from Task import Task


class StabilizeSteering(Task):

    def __init__(self):
        self.center = (960, 540)
        super().__init__()

    def _solve(self, frame):
        self.set_pos(*self.center)
        self.sleep(.1)
        self.click()
        self.sleep(1.1)
        return True


if __name__ == '__main__':
    from time import sleep
    sleep(2)
    stabilize_steering = StabilizeSteering()
    stabilize_steering.solve()
