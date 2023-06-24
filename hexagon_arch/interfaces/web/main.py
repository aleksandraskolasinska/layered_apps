from flask import Flask, render_template
from hexagon_arch.adapters.controllers.task_controller import TaskController
from hexagon_arch.adapters.repositories.in_memory_task_repository import InMemoryTaskRepository

app = Flask(__name__)

@app.route('/')
def index():
    task_controller = TaskController(InMemoryTaskRepository())
    tasks = task_controller.get_all_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task_description = request.form['description']
    task_controller.add_task(task_description)
    return redirect('/')

if __name__ == '__main__':
    app.run()
