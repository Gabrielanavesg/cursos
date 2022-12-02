from flask import Flask, render_template, request

app = Flask(__name__)

cursos = [
    {'curso': 'Administração', 'area': 'Humanas'},
    {'curso': 'Direito', 'area': 'Humanas'},
    {'curso': 'Arquitetura', 'area': 'Sociais'},
    {'curso': 'Historia', 'area': 'Humanas'},
    {'curso': 'Engenharia Civil', 'area': 'Exatas'}
]

@app.route('/')
def home():
    return render_template('home.html', cursos=cursos)

@app.route('/create', methods=['POST'])
def create():
    nomecurso = request.form['nomecurso']
    areacurso = request.form['areacurso']
    curso = {'curso': nomecurso, 'area': areacurso}
    cursos.append(curso)
    return render_template('home.html', cursos=cursos)

@app.route('/delete/<int:id>')
def delete(id):
    for curso in cursos:
        id = i =+ 1
    cursos.pop(id)
    return render_template('home.html', cursos=cursos, id=id)

app.run(debug=True)