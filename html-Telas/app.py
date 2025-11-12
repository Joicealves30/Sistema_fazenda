# ...existing code...
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/funcionarios')
def funcionarios():
    return render_template('funcionarios.html')

@app.route('/estoque')
def estoque():
    return render_template('estoque.html')

@app.route('/maquinarios')
def maquinarios():
    return render_template('maquinarios.html')

if __name__ == '__main__':
    app.run(debug=True)
