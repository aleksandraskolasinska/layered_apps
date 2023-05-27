from flask import Flask, render_template, request, redirect
from adapters.controllers.task_controller import TaskController


app = Flask(__name__)


task_controller = TaskController()

@app.route('/', methods=['GET'])
def tasks():
    tasks = task_controller.get_all_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task_description = request.form['description']
    task_controller.add_task(task_description)
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run()
