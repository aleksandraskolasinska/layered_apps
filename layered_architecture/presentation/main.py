from flask import Flask, render_template, request, redirect
from business_logic.services import TaskService
from dependencies.login_service import LoginService

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', tasks=TaskService.get_all_tasks())

@app.route('/add_task', methods=['POST'])
def add_task():
    task_description = request.form['task_description']
    TaskService.add_task(task_description)
    return redirect('/')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if LoginService.login(username, password):
            session['username'] = username
            return redirect('/')
        else:
            return render_template('login.html', message='Invalid credentials')
    else:
        return render_template('login.html')

if __name__ == '__main__':
    app.run()
