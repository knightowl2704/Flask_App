from flask import Flask, json, request, render_template
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import input_required, length
from flaskext.mysql import MySQL
import  pymysql.connections

app = Flask(__name__)
app.secret_key = 'developmentkey'
app.config["RECAPTCHA_PUBLIC_KEY"] = '#######################################'
app.config["RECAPTCHA_PRIVATE_KEY"] = '#######################################'
app.config["TESTING"] = True

mysql = MySQL()



class LoginForm(FlaskForm):
    username = StringField("Username", validators=[input_required()])
    password = PasswordField("Password",validators=[input_required()])
    recaptcha = RecaptchaField()


# @app.route('/')
# def entry_page():
#     # Jinja template of the webpage
#     return render_template('index.html')

@app.route('/',methods = ['POST','GET'])
def form():
   form = LoginForm()
   if form.validate():
       return "Form is submitted"
   return render_template('index.html', form = form)

if __name__ == '__main__':
    app.run(debug=False)


