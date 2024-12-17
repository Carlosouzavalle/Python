from main import app
from flask import render_template

@app.route("/")
def calculator():
    return render_template("index.html")