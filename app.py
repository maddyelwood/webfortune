from flask import Flask, render_template
app = Flask(__name__)

import subprocess
import cowsay

@app.route('/')
def index():
    return redirect(url_for('fortune'))

@app.route('/fortune/', methods=['GET'])
def fortune():
    fortune = subprocess.check_output("fortune", shell=True)
    return '<pre>' + fortune.decode("utf-8") + '</pre>'

@app.route('/cowsay/<message>/', methods=['GET'])
def cowsay(message):
    return cowsay.cow(message)

@app.route('/cowfortune/', methods=['GET'])
def pipe_fortune():
    pass

