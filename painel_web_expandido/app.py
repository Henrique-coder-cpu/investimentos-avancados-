from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import os

app = Flask(__name__)
app.secret_key = 'segredo'

DB_PATH = 'banco.db'

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS anuncios (id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT NOT NULL, ganho REAL NOT NULL)")
        conn.commit()

@app.route('/', methods=['GET', 'POST'])
def login():
    erro = None
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == '1234':
            session['usuario'] = 'admin'
            return redirect(url_for('painel'))
        else:
            erro = 'Credenciais inválidas'
    return render_template('login.html', erro=erro)

@app.route('/painel')
def painel():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM anuncios")
        anuncios = c.fetchall()
        total = sum([a[2] for a in anuncios])
    return render_template('painel.html', anuncios=anuncios, total=total)

@app.route('/adicionar', methods=['POST'])
def adicionar():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    titulo = request.form['titulo']
    ganho = float(request.form['ganho'])
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("INSERT INTO anuncios (titulo, ganho) VALUES (?, ?)", (titulo, ganho))
        conn.commit()
    return redirect(url_for('painel'))

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    if 'usuario' not in session:
        return redirect(url_for('login'))
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        if request.method == 'POST':
            titulo = request.form['titulo']
            ganho = float(request.form['ganho'])
            c.execute("UPDATE anuncios SET titulo=?, ganho=? WHERE id=?", (titulo, ganho, id))
            conn.commit()
            return redirect(url_for('painel'))
        else:
            c.execute("SELECT * FROM anuncios WHERE id=?", (id,))
            anuncio = c.fetchone()
    return render_template('editar.html', anuncio=anuncio)

@app.route('/excluir/<int:id>')
def excluir(id):
    if 'usuario' not in session:
        return redirect(url_for('login'))
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute("DELETE FROM anuncios WHERE id=?", (id,))
        conn.commit()
    return redirect(url_for('painel'))

@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
