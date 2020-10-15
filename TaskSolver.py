from TaskIdentifier import TaskIdentifier
from tasks.FixWiring import FixWiring


class TaskSolver:
    def __init__(self):
        pass

    @staticmethod
    def from_task_id_to_object(task_id):
        task_name = ''.join([name.capitalize() for name in task_id.split('-')])


if __name__ == '__main__':
    print(TaskSolver.from_task_id_to_object('empty-chute'))
