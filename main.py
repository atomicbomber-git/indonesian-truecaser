from flask import Flask, jsonify, request, render_template
import waitress
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.jinja2")

waitress.serve(app, host="0.0.0.0", port=8081)