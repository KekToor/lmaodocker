from flask import Flask, render_template, request, redirect, flash, url_for  # import flask

app = Flask(__name__)             # create an app instance
app.secret_key="kjshfkjsdhfkjsdhfkjsdh"
@app.route("/")                   # at the end point /
def ahoj():                      # call method hello
    return "Hello World!"         # which returns "hello world"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name="Kamos"):
    pole=["jedna","dvě","tři"]
    return render_template('script.html', name=name, pole=pole)
from wtforms import Form, BooleanField, StringField, PasswordField, validators, FloatField


class RegistrationForm(Form):
    a = FloatField('Value a', [validators.NumberRange(0, 10)])
    b = FloatField('Value b', [validators.NumberRange(0, 10)])

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        flash('Thanks for registering')
        return str(int(form.a.data) + int(form.b.data))
    return render_template('register.html', form=form)
