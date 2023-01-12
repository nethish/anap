from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
  return "hello there"

@app.route('/<name>')
def name(name):
  return "hello " + name 
