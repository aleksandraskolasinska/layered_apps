from business_logic.models import Task
from data_access.repositories import TaskRepository

class TaskService:
    @staticmethod
    def get_all_tasks():
        return TaskRepository.get_all_tasks()

    @staticmethod
    def add_task(description):
        task = Task(description)
        TaskRepository.save_task(task)
