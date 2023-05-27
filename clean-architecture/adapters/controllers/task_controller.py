from adapters.repositories.task_repository_impl import TaskRepositoryImpl
from core.entities.task import Task

task_repository = TaskRepositoryImpl()

class TaskController:
    def get_all_tasks(self):
        return task_repository.get_all_tasks()

    def add_task(self, description):
        task = Task(description)
        task_repository.add_task(task)
