from . import Task


class ClearAsteroids(Task):

    def __init__(self):
        self.avoid_asteroids = (960, 940)
        self.y_range = range(143, 800, 4)
        self.x_columns = [1160, 881]
        self.x_columns = [1360, 1160, 881]
        self.x_columns = [1360, 1160, 560]
        self.x_column = self.x_columns[0]
        self.asteroid_color = (55, 112, 66)
        super().__init__()

    def identify_asteroid(self, pixels):
        for y in self.y_range:
            if pixels[self.x_column, y] == self.asteroid_color:
                return self.x_column, y

    def _solve(self, frame):
        pixels = frame.load()

        for x_index in range(len(self.x_columns)):
            self.x_column = self.x_columns[x_index]
            xy = self.identify_asteroid(pixels)
            if xy is not None:
                self.click(xy)
                break

        if pixels[1410, 91][0] == 0:
            return True

        self.click(*self.avoid_asteroids)


if __name__ == '__main__':
    from time import sleep
    sleep(2)
    clear_asteroids = ClearAsteroids()
    clear_asteroids.solve()
