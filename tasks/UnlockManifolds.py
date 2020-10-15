import sys; sys.path.append("..")
from utils import image_in_another, dhash_calc
from .Task import Task
from PIL import Image

"""
    @staticmethod
    def process_images():
        from PIL import Image
        for n in range(1, 11):
            Image.open(f"unlock-manifolds-numbers-images/{n}.jpg").crop((32, 32, 64 + 32, 64 + 32)).save(f"unlock-manifolds-numbers-images-resizes/{n}.jpg")

    def _solve(self, frame):

        for pos in self.squares_positions:
            #print((*pos, pos[0] + 137, pos[1] + 137))
            numb = frame.crop((*pos, pos[0] + 137, pos[1] + 137))
            x = input("[?] Put the number to this picture: ")
            numb.save(f"unlock-manifolds-numbers-images/{x}.jpg")

        return True
"""


class UnlockManifolds(Task):

    def __init__(self):
        self.images = []

        self.order = [None for _ in range(10)]
        self.squares_positions = UnlockManifolds.fill_squares_positions(start=[585, 394], columns=5, rows=2)
        super().__init__()

    @staticmethod
    def fill_squares_positions(start, columns, rows) -> list:
        squares_positions = []

        size = 137
        x_padding = 16
        y_padding = 17  # Idk why but it looks like the y padding value is different from the x padding value, anyway

        for row in range(rows):
            for column in range(columns):
                square_position = start.copy()

                square_position[0] += (x_padding + size) * column
                square_position[1] += (y_padding + size) * row

                squares_positions.append(square_position)

        return squares_positions

    @staticmethod
    def resized_square(position, frame):
        return frame.crop((position[0] + 32, position[1] + 32, position[0] + 96, position[1] + 96))

    def open_images(self):
        self.images = [Image.open(f"unlock-manifolds-numbers-images-resized/{index}.jpg") for index in range(1, 11)]

    def close_images(self):
        assert self.images, "\n\n[!] Run UnlockManifolds.open_images(self) before using close_images."
        for image in self.images:
            image.close()
        self.images.clear()

    def find_similar_index(self, blue_square):
        assert self.images, "\n\n[!] Run UnlockManifolds.open_images(self) before using find_similar\nand remember to run close_images after."

        for index, comparision_image in enumerate(self.images):
            if image_in_another(comparision_image, blue_square, bit_diff=30):
                return index

    def _solve(self, frame):
        index_order = []

        self.open_images()
        for blue_square_position in self.squares_positions:
            blue_square = UnlockManifolds.resized_square(blue_square_position, frame)
            index_order.append(self.find_similar_index(blue_square))
        self.close_images()

        for square_click_index in range(10):
            square_position_index = index_order.index(square_click_index)
            self.click(self.squares_positions[square_position_index])

        return True


if __name__ == '__main__':
    from time import sleep
    sleep(2)
    unlock_manifolds = UnlockManifolds()
    unlock_manifolds.solve()
