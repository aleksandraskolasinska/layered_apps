from core.entities.task import Task
from core.interfaces.task_repository import TaskRepository


class TaskUseCases:
    def __init__(self):
        self.task_repository = TaskRepository()

    def get_all_tasks(self):
        return self.task_repository.get_all_tasks()

    def add_task(self, description):
        task = Task(description)
        self.task_repository.add_task(task)