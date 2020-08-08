from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Saber!'

@app.route('/calculator/<int:number>/<int:number2>')
def calculator(number , number2):
    all =  number * number2
    return render_template('hello.html', all=all)
