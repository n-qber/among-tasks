from .Task import Task


class EmptyChute(Task):

    def __init__(self):
        self.drag_start_position = (1270, 466)
        self.drag_finish_position = (1270, 760)
        super().__init__()

    def _solve(self, frame):
        self.set_pos(*self.drag_start_position)
        self.click_down()
        self.dragTo(*self.drag_finish_position, mouseDownUp=False)
        self.sleep(1.5)
        self.click_up()
        return True


if __name__ == '__main__':
    from time import sleep
    sleep(2)
    empty_chute = EmptyChute()
    empty_chute.solve()
