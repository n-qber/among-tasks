from Task import Task


class FixWiring(Task):

    def __init__(self):
        self.drag_pos = 600
        self.left_x_pos = 556
        self.right_x_pos = 1333
        self.heights = [275, 464, 646, 825]
        super().__init__()

    def identify_colors(self, frame, side):
        if side == "left":
            x_pos = self.left_x_pos
        elif side == "right":
            x_pos = self.right_x_pos
        else:
            assert False, "\n\n[!] Side was not specified correctly ->: side=\"left\""

        pixels = frame.load()
        return [pixels[x_pos, height] for height in self.heights]

    def fix_by_position(self, pos0, pos1):
        self.set_pos(*pos0)
        self.sleep(.1)
        self.click_down()
        self.sleep(.1)
        self.set_pos(*pos1)
        self.sleep(.1)
        self.click_up()

    def fix_by_index(self, left_index, right_index):
        pos0 = (self.drag_pos, self.heights[left_index])
        pos1 = (self.right_x_pos, self.heights[right_index])
        self.fix_by_position(pos0, pos1)

    def _solve(self, frame):
        left_colors = self.identify_colors(frame, "left")
        right_colors = self.identify_colors(frame, "right")

        for left_index, left_color in enumerate(left_colors):
            right_index = right_colors.index(left_color)
            self.fix_by_index(left_index, right_index)
        return True


if __name__ == '__main__':
    from time import sleep
    sleep(2)
    fix_wiring = FixWiring()
    fix_wiring.solve()
