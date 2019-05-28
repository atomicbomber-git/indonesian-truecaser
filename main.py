#!

from flask import Flask, jsonify, request, render_template
import argparse
import waitress
import truecaser

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    output_text = None
    input_text = None

    if request.method == "POST":
        # Remember old input
        input_text = request.form["input_text"]
        output_text = truecaser.process(request.form["input_text"])

    return render_template("index.jinja2", input_text=input_text, output_text=output_text)

@app.route("/handle", methods=["POST"])
def handle():
    text = request.form.get_json()
    return jsonify(text)

# Default host and default port
host = "0.0.0.0"
port = 8081

# Parse command line arguments
argument_parser = argparse.ArgumentParser()
argument_parser.add_argument(
    "--host",
    nargs='?',
    help="Host on which the server will run. Example: 192.168.7.1",
    default=host
)
argument_parser.add_argument("--port",
    nargs='?',
    help="Port on which the server will run. Example: 8083",
    default=port
)

arguments = argument_parser.parse_args()
waitress.serve(app, host=arguments.host, port=arguments.port)
