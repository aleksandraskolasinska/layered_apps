from hexagon_arch.core.entities.task import Task

class InMemoryTaskRepository:
    def __init__(self):
        self.tasks = []

    def get_all_tasks(self):
        return self.tasks

    def add_task(self, task_description):
        task = Task(description=task_description)
        self.tasks.append(task)
