import pygame as pg
import pyperclip
import os.path
from PIL import Image

image = ""
_image = image
window = pg.display.set_mode((1920, 1080), pg.FULLSCREEN)
start_pos = []

while True:
    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            pg.quit()
            exit(0)

        if ev.type == pg.KEYDOWN:
            if ev.dict.get("unicode") == 'o':
                try:
                    _image = image
                    image = pyperclip.paste()
                    window.fill((0, 0, 0))
                    window.blit(pg.image.load(image), (0, 0))
                except pg.error:
                    image = _image
                    print(f"[x] Error, got: {pyperclip.paste()}")

        elif ev.type == pg.MOUSEBUTTONDOWN:
            start_pos = pg.mouse.get_pos()
        elif ev.type == pg.MOUSEBUTTONUP:
            end_pos = pg.mouse.get_pos()

            print(start_pos, end_pos)

            if start_pos and image:
                name = os.path.splitext(image)[0] + f"__{start_pos[0]}x{start_pos[1]}__{end_pos[0]}x{end_pos[1]}.jpg"
                img = Image.open(image)
                img.crop((*start_pos, *end_pos)).save(name)

                from json import load, dump
                with open("tasks.json", "r") as tasks_dot_json:
                    tasks_json = load(tasks_dot_json)

                path = name.lstrip(os.getcwd()).lstrip("\\")
                tasks_json.append(dict(name=os.path.splitext(os.path.split(image)[-1])[0],
                     pos=start_pos,
                     path=path))

                with open("tasks.json", "w") as tasks_dot_json:
                    dump(tasks_json, tasks_dot_json, indent=4)

    pg.display.update()
