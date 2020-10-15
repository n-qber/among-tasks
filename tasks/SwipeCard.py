from .Task import Task


class SwipeCard(Task):

    def __init__(self):
        self.wallet_card_position = (850, 830)
        self.card_swipe_start_position = (666, 404)
        self.card_swipe_start_position = (666, 404)
        self.card_swipe_end_position = (1395, 404)

        self.y_offset = 37

        super().__init__()

    def _solve(self, frame):
        self.set_pos(*self.wallet_card_position)
        self.dragTo(*self.card_swipe_start_position, .11)
        self.sleep(.4)
        self.click_down()
        for _ in range((self.card_swipe_end_position[0] - self.card_swipe_start_position[0]) // self.y_offset + 1):
            self.move(self.y_offset, 0)
        self.click_up()

        return True


if __name__ == '__main__':
    from time import sleep
    sleep(2)
    swipe_card = SwipeCard()
    swipe_card.solve()
