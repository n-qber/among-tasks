from .Task import Task


class PrimeShields(Task):

    def __init__(self):
        self.shield_points = [
            (970, 360),
            (970, 540),
            (1160, 420),
            (780, 460),
            (800, 600),
            (990, 720),
            (1141, 620),
        ]
        super().__init__()

    def _solve(self, frame):
        pixels = frame.load()

        for shield_point in self.shield_points:
            if pixels[shield_point][1] < 110:
                self.click(*shield_point)

        return True


if __name__ == '__main__':
    from time import sleep
    sleep(2)
    prime_shields = PrimeShields()
    prime_shields.solve()
