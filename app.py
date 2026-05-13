"""
App.py
    Código principal da aplicação
"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template('welcome.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route("/courses")
def courses():
    return render_template('courses.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/about")
def about():
    return render_template('about.html')


