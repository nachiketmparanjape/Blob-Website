from flask import Flask, render_template, request, session

from src.common.database import Database
from src.models.user import User

app = Flask(__name__) # '__main__'
app.secret_key = "nachiket"



@app.route('/')
def hello_method():
    #return ("Hello, world!")
    return render_template('login.html')

@app.before_first_request
def initialize_database():
    Database.initialize()


"""Check user email and password from database using method user
and then render profile.html if true"""
@app.route('/login', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']

    if User.login_valid(email,password):
        User.login(email)

    return render_template("profile.html",email=session['email'])


if __name__ == '__main__':
    app.run()

