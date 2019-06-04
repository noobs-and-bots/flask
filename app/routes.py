from app import app
from flask import Flask, send_from_directory

@app.route('/')
@app.route('/index')

def index():
    return 'Siema'

@app.route('/files/<path:path>')
def send_file(path):
    return send_from_directory('files', path)
