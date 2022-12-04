from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

URL = "https://5000-jooshica-cursos-4amhp5x5f07.ws-us77.gitpod.io"

import csv

cursos = []

leitura = open('cursos.csv')

ler = csv.DictReader(leitura)

for curso in ler:
    curso = {'curso': curso['curso'], 'area': curso['area']}
    cursos.append(curso)

leitura.close()

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

@app.route('/delete')
def delete():
    return render_template('delete.html')

@app.route('/deletar', methods=['POST'])
def deletar():
    removercurso = request.form['deletarcurso']
    removerarea = request.form['deletararea']        
    curso_removido = { 'curso': removercurso, 'area': removerarea}
    if curso_removido in cursos:
        cursos.remove(curso_removido)
    else:
        return render_template('cursonaoencontrado.html')

    return redirect(URL)

@app.route('/save')
def save():
    return render_template('salvar.html')

@app.route('/salvar', methods=['POST'])
def salvar():
    with open('cursos.csv', 'wt') as salvar:
        save = csv.DictWriter(salvar, ['curso', 'area']) 
        save.writeheader()
        save.writerows(cursos)
        return redirect(URL)

app.run(debug=True)