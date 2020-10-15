from TaskIdentifier import TaskIdentifier
from pynput.keyboard import Listener, Key
import importlib


class TaskSolver:
    def __init__(self):
        self.identifier = TaskIdentifier()

    @staticmethod
    def from_task_id_to_object(task_id):
        task_name = ''.join([name.capitalize() for name in task_id.split('-')])
        return getattr(importlib.import_module(f"tasks.{task_name}"), task_name)

    def on_press(self, key):
        if key == Key.space:
            try:
                task = TaskSolver.from_task_id_to_object(self.identifier.identify_task())()
                task.solve()
            except Exception as ex:
                pass

    def start_listening_keyboard(self):
        with Listener(on_press=self.on_press) as listener:
            listener.join()

    def start(self):
        self.start_listening_keyboard()


if __name__ == '__main__':
    task_solver = TaskSolver()
    task_solver.start()
