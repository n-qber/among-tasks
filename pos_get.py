from pynput.keyboard import Listener
from pynput.mouse import Controller

positions = []


def state(position, reset=False, save=False):
    global positions

    if reset:
        positions = []
        print(f"[*] Reseting: {positions}")
        return

    if save:
        with open("use_positions.txt", "a") as f:
            f.write(', '.join([str(x) for x in positions]))
            f.write('\n')
        print(f"[*] Saving: {positions}")
        return

    positions.append(position)
    if len(positions) == 1:
        print(f"[*] First:  {positions[0]}")
    elif len(positions) == 2:
        print(f"[*] Second: {', '.join([str(x) for x in positions])}")
    else:
        print(f"[*] Won't override: press \"R\"")


def on_press(key):
    if hasattr(key, "char"):
        if key.char == 'p':
            state(Controller().position)
        elif key.char == 'r':
            state(0, reset=True)
        elif key.char == 's':
            state(0, save=True)


with Listener(on_press=on_press) as l:
    l.join()
