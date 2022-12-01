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

#@app.route('/Deletar<int:curso', methods['POST'])
def deletar(curso):
    curso = request.form('nomecurso') 
    curso = request.form('areacurso')
    cursos.remove(curso)
    return render_template('home.html', cursos=cursos)   

print('teste sincronizar')

app.run(debug=True)