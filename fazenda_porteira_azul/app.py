from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

# Página de funcionários
@app.route('/funcionarios')
def funcionarios():
    return render_template('funcionarios.html')

# Página para adicionar funcionário
@app.route('/add_funcionarios', methods=['GET', 'POST'])
def add_funcionarios():
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        sexo = request.form['sexo']
        cpf = request.form['cpf']
        telefone = request.form['telefone']
        endereco = request.form['endereco']
        cargo = request.form['cargo']
        print(f'Novo funcionário adicionado: {nome}, {idade}, {sexo}, {cpf}, {telefone}, {endereco}, {cargo}')
        return redirect(url_for('funcionarios'))
    return render_template('add_funcionarios.html')

if __name__ == '__main__':
    app.run(debug=True)
