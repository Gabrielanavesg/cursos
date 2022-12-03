from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

URL = "https://5000-jooshica-cursos-ju9gm0rfcss.ws-us77.gitpod.io"

cursos = [
    {'curso': 'Administração'},
    {'curso': 'Direito'},
    {'curso': 'Arquitetura'},
    {'curso': 'História'},
    {'curso': 'Engenharia Civil'}
]

@app.route('/')
def home():
    return render_template('home.html', cursos=cursos)

@app.route('/create', methods=['POST'])
def create():
    nomecurso = request.form['nomecurso']
    curso = {'curso': nomecurso}
    cursos.append(curso)
    return render_template('home.html', cursos=cursos)

@app.route('/delete')
def delete():
    return render_template('delete.html')

@app.route('/deletar', methods=['POST'])
def deletar():
    removercurso = request.form['deletarcurso']
    curso_removido = { "curso": removercurso}
    cursos.remove(curso_removido)
          
    return redirect(URL)


app.run(debug=True)