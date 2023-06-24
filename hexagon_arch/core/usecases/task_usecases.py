class TaskUseCases:
    def __init__(self, task_repository):
        self.task_repository = task_repository

    def get_all_tasks(self):
        return self.task_repository.get_all_tasks()

    def add_task(self, task_description):
        self.task_repository.add_task(task_description)
