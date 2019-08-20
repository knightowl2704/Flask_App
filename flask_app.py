from flask import Flask, json, request, render_template
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import input_required, length
from flaskext.mysql import MySQL
import  pymysql.connections

app = Flask(__name__)
app.secret_key = 'developmentkey'
app.config["RECAPTCHA_PUBLIC_KEY"] = 'YOUR_RECAPTCHA_PUBLIC_KEY_HERE(v2)'
app.config["RECAPTCHA_PRIVATE_KEY"] = 'YOUR_RECAPTCHA_PRIVATE_KEY_HERE(v2)'
app.config["TESTING"] = True

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'YOUR_DATABASE_USERNAME'
app.config['MYSQL_DATABASE_PASSWORD'] = 'YOUR_DATABASE_PASSWORD_HERE'
app.config['MYSQL_DATABASE_DB'] = 'flaskappdata' #DATABASE_NAME

mysql = MySQL(app)



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

       if request.method == 'POST':
           details = request.form
           username = details['username']
           password1 = details['password']
           z = mysql.connect()
           cur = z.cursor()
           cur.execute("INSERT INTO flaskappdata(username,password1) VALUES (%s,MD5(%s))" , (username, password1))
           z.commit()
           cur.close()
           return 'success'

   return render_template('index.html', form = form)

if __name__ == '__main__':
    app.run(debug=False)


