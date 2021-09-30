from flask import Flask, render_template          # import flask

app = Flask(__name__)             # create an app instance

@app.route("/")                   # at the end point /
def ahoj():                      # call method hello
    return "Hello World!"         # which returns "hello world"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name="Kamos"):
    pole=["jedna","dvě","tři"]
    return render_template('script.html', name=name, pole=pole)
