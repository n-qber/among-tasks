from Task import Task


class AcceptDiverted(Task):

    def __init__(self):
        self.accept_position = (960, 540)
        super().__init__()

    def _solve(self, frame):
        self.click(*self.accept_position)
        return True


if __name__ == '__main__':
    from time import sleep
    sleep(2)
    accept_diverted = AcceptDiverted()
    accept_diverted.solve()
