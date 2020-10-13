from Task import Task


class AlignEngine(Task):

    def __init__(self):
        self.width_range = 1320, 1243
        self.height_range = 150, 930
        super().__init__()

    def _solve(self, frame):
        pixels = frame.load()
        for y in range(*self.height_range):
            for rang in [(*self.width_range, -1), (self.width_range[::-1])]:
                for x in range(*rang):
                    print(x, y)

        return True


if __name__ == '__main__':
    from time import sleep
    sleep(2)
    align_engine = AlignEngine()
    align_engine.solve()
