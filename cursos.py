from flask import Flask, render_template, request

app = Flask(__name__)

cursos = [
    {'curso': 'Administração', 'area': 'Humanas'},
    {'curso': 'Direito', 'area': 'Humanas'}
    {'curso': 'Arquitetura', 'area': 'Sociais'}
    {'curso': 'Historia', 'area': 'Humanas'}
    {'curso': 'Engenharia Civil', 'area': 'Exatas'}
]

@app.route('/')
def home():
    return render_template('home.html', cursos=cursos)