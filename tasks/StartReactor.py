from Task import Task
from statistics import mean


class StartReactor(Task):

    def __init__(self):
        self.squares = [
            (525, 490), (657, 476), (782, 472),
            (523, 605), (648, 596), (772, 601),
            (522, 732), (649, 715), (780, 734)
        ]
        self.squares_supplement_to_buttons = 612

        self.button_position = 1260, 600

        self.button_enabled_color = mean((209, 208, 209))
        self.button_disabled_color = mean((116, 115, 116))
        self.blue_color = mean((68, 168, 255))

        self.feedback_green_light_position = (810, 320)
        self.feedback_green_light_color = mean((0, 192, 0))

        self.imitate = []

        self.waiting_black = False
        super().__init__()

    def press_right_buttons(self):
        for square_position in self.imitate:
            self.click(square_position[0] + self.squares_supplement_to_buttons, square_position[1])

    def _solve(self, frame):
        pixels = frame.load()

        for square_position in self.squares:

            if abs(mean(pixels[square_position]) - self.blue_color) < 5:
                if not self.waiting_black:
                    self.imitate.append(square_position)
                    self.waiting_black = True
                return False

        self.waiting_black = False

        if abs(mean(pixels[self.button_position]) - self.button_enabled_color) < 2:

            self.press_right_buttons()
            self.imitate.clear()

            #If it is the last one stop solving
            return abs(mean(pixels[self.feedback_green_light_position]) - self.feedback_green_light_color) < 5


if __name__ == '__main__':
    from time import sleep
    sleep(2)
    start_reactor = StartReactor()
    start_reactor.solve()

