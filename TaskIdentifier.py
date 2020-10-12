from PIL import ImageGrab, Image
from utils import start_timeout, timeout
from json import load
import dhash


class TaskIdentifier:

    with open("tasks.json") as tkjson:
        tasks = load(tkjson)

    @staticmethod
    def dhash(img: Image) -> int:
        return int(dhash.format_hex(*dhash.dhash_row_col(img)), 16)

    @staticmethod
    def image_in_another(another: Image, image: Image, pos: list) -> bool:
        if type(image) is str:
            image = Image.open(image)
        if type(another) is str:
            another = Image.open(another)

        width = image.width
        height = image.height

        start_x, start_y = pos

        image_dhash = TaskIdentifier.dhash(image)
        another_dhash = TaskIdentifier.dhash(another.crop((start_x, start_y, start_x + width, start_y + height)))

        return dhash.get_num_bits_different(image_dhash, another_dhash) < 20

    @staticmethod
    def identify_task():
        start = start_timeout()

        while timeout(start) < 2.5:
            image = ImageGrab.grab()
            for task in TaskIdentifier.tasks:
                name = task["name"]
                pos = task["pos"]

                if TaskIdentifier.image_in_another(image, task["path"], pos):
                    #print(f"[I] Identified task: {name}")
                    return name


if __name__ == '__main__':
    from pynput.keyboard import Listener

    def on_press(key):
        try:
            if key.char == "p":
                task_id = TaskIdentifier.identify_task()
                if task_id:
                    print(f"[I] Identified task: {task_id}")
        except:
            pass

    with Listener(on_press=on_press) as j:
        j.join()
