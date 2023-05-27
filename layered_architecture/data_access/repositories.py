class TaskRepository:
    tasks = []  

    @staticmethod
    def get_all_tasks():
        return TaskRepository.tasks

    @staticmethod
    def save_task(task):
        TaskRepository.tasks.append(task)
