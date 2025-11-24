from flask import Flask, request, render_template, session, redirect, url_for, flash
import sqlite3
import os
import hashlib

app = Flask(__name__)

# Clave secreta fija y configuración segura de sesión
app.config['SECRET_KEY'] = 'CAMBIA_ESTA_CLAVE_POR_UNA_LARGA_Y_UNICA'

app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SECURE=False,  
    SESSION_COOKIE_SAMESITE="Strict"
)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


@app.route('/')
def index():
    return 'Welcome to the Task Manager Application!'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()

        # Siempre usar consultas parametrizadas + hash de la contraseña
        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        hashed_password = hash_password(password)
        user = conn.execute(query, (username, hashed_password)).fetchone()

       
        if user:
            session['user_id'] = user['id']
            session['role'] = user['role']
            return redirect(url_for('dashboard'))
        else:
            return 'Invalid credentials!'
    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''


@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user_id = session['user_id']
    conn = get_db_connection()
    tasks = conn.execute(
        "SELECT * FROM tasks WHERE user_id = ?", (user_id,)).fetchall()
    conn.close()

    return render_template('dashboard.html', user_id=user_id, tasks=tasks)


@app.route('/add_task', methods=['POST'])
def add_task():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    task = request.form['task']
    user_id = session['user_id']

    conn = get_db_connection()
    conn.execute(
        "INSERT INTO tasks (user_id, task) VALUES (?, ?)", (user_id, task))
    conn.commit()
    conn.close()

    return redirect(url_for('dashboard'))


@app.route('/delete_task/<int:task_id>')
def delete_task(task_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    conn = get_db_connection()
    conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

    return redirect(url_for('dashboard'))


@app.route('/admin')
def admin():
    if 'user_id' not in session or session.get('role') != 'admin':
        return redirect(url_for('login'))

    return 'Welcome to the admin panel!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

