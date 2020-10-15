import dhash
from time import time
from PIL import Image


def timeout(start):
    return time() - start


def start_timeout():
    return time()


def use_button_pos():
    return (1691, 850), (1896, 1053)


def dhash_calc(img) -> int:
    return int(dhash.format_hex(*dhash.dhash_row_col(img)), 16)


def image_in_another(another: Image, image: Image, pos: list=(0, 0), bit_diff=20) -> bool:
    if type(image) is str:
        image = Image.open(image)
    if type(another) is str:
        another = Image.open(another)

    width = image.width
    height = image.height

    start_x, start_y = pos

    image_dhash = dhash_calc(image)
    another_dhash = dhash_calc(another.crop((start_x, start_y, start_x + width, start_y + height)))

    return dhash.get_num_bits_different(image_dhash, another_dhash) < bit_diff