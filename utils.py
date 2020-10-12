from time import time


def timeout(start):
    return time() - start


def start_timeout():
    return time()


def use_button_pos():
    return (1691, 850), (1896, 1053)
