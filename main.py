from flask import Flask, jsonify, request, render_template
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

waitress.serve(app, host="0.0.0.0", port=8081)