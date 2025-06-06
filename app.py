from flask import Flask, render_template, request, redirect
import sqlite3

""" Criação do Banco de Dados
conn = sqlite3.connect('tarefas.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS tarefas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        descricao TEXT
)
''')

conn.commit()
conn.close()

"""

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('tarefas.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    tarefas = conn.execute('SELECT * FROM tarefas').fetchall()
    conn.close()
    return render_template('index.html', tarefas = tarefas)

@app.route('/add', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        conn = get_db_connection()
        conn.execute('INSERT INTO tarefas (titulo, descricao) VALUES (?, ?)', (titulo, descricao))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('form.html')

@app.route('/edit/<int:id>', methods=('GET', 'POST'))
def edit(id):
    conn = get_db_connection()
    tarefa = conn.execute('SELECT * FROM tarefas WHERE id = ?', (id,)).fetchone()

    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        conn.execute('UPDATE tarefas SET titulo = ?, descricao = ? WHERE id = ?', (titulo, descricao, id))
        conn.commit()
        conn.close()
        return redirect('/')
    
    conn.close()
    return render_template('form.html', tarefa=tarefa)

@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM tarefas WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
