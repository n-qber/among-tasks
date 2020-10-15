from .Task import Task


class FuelEngines(Task):

    def __init__(self):
        self.fuel_position = (1470, 880)
        super().__init__()

    def _solve(self, frame):
        self.set_pos(*self.fuel_position)
        self.sleep(.1)
        self.click_down()
        self.sleep(3.1)
        self.click_up()
        return True


if __name__ == '__main__':
    from time import sleep
    sleep(2)
    fuel_engines = FuelEngines()
    fuel_engines.solve()
