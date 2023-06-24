from hexagon_arch.core.usecases.task_usecases import TaskUseCases

class TaskController:
    def __init__(self, task_usecases):
        self.task_usecases = task_usecases

    def get_all_tasks(self):
        return self.task_usecases.get_all_tasks()
