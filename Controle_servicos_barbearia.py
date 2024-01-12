from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Agenda de horários
agenda = {f'{i:02d}:00': None for i in range(9, 22)}

# Rota principal para exibir a página de agendamento
@app.route('/')
def index():
    return render_template('index.html', agenda=agenda)

# Rota para processar o formulário de agendamento
@app.route('/agendar', methods=['POST'])
def agendar():
    if request.method == 'POST':
        horario = request.form['horario']
        nome = request.form['nome']
        servico = request.form['servico']

        if horario in agenda and agenda[horario] is None:
            agenda[horario] = {'Nome': nome, 'Servico': servico}
            return redirect(url_for('index'))
        else:
            return "Horário indisponível. Escolha outro horário."

# Rota para cancelar um agendamento
@app.route('/cancelar/<horario>')
def cancelar(horario):
    if horario in agenda and agenda[horario] is not None:
        agenda[horario] = None
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
