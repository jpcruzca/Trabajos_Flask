from flask import Flask, request, render_template
from wtforms import Form, StringField, PasswordField, BooleanField


app = Flask( __name__, template_folder='template')

class RegistrationForm(Form):
    username = StringField('username')
    password = PasswordField('New Password')
    ideas = StringField('some ideas')

class LoginForm(Form):
    username = StringField('username')
    password = PasswordField('New Password')

class InfoForm(Form):
    interest = StringField('Do you have any particular interest? tell us..')
    student = BooleanField('Are you University Student?')

@app.route('/register', methods=['GET','POST'])
def index():
    form = RegistrationForm()
    print(request.method)
    data = ''
    if request.method == 'POST':#Hay un problema con el método post, revisar
        data = request.form
        print(data)
    return render_template('register.html', form=form, data = data )


@app.route('/a', methods=['GET','POST'])
def login():
    logform = LoginForm()
    data = ''
    if request.method == 'POST':
        data = request.form
        print(data)
    return render_template('login.html', logform=logform )



if __name__== '__main__':
	app.run(debug=True, port=8000)