from flask import Flask, render_template, redirect, url_for, request, session, jsonify, abort
app = Flask(__name__)

import subprocess

@app.route('/')
def index():
    return redirect(url_for('fortune'))

@app.route('/fortune/', methods=['GET'])
def fortune():
    fortune = subprocess.check_output("fortune", shell=True)
    return '<pre>' + fortune.decode("utf-8") + '</pre>'

@app.route('/cowsay/<message>/', methods=['GET'])
def cowsay(message):
    cow = subprocess.check_output('cowsay -f turtle ' + message, shell=True)
    return '<pre>' + cow.decode("utf-8") + '</pre>'

@app.route('/cowfortune/', methods=['GET'])
def pipe_fortune():
    cowfortune = subprocess.run('fortune | cowsay -f turtle ', stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    return '<pre>' + cowfortune.stdout.decode('utf-8') + '</pre>'

    #extra cows found here:
    #/usr/share/cowsay/cow
