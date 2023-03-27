from flask import Flask, render_template, url_for, request, flash
from flask_login import UserMixin
import psycopg2

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisasecretkey'


@app.route('/', methods=['post', 'get'])
def home():
    conn = psycopg2.connect("postgresql://postgres:postgres@localhost:5432/licenta")
    crsr = conn.cursor()
    crsr.execute('SELECT current_date, current_time ')
    db_version = crsr.fetchall()
    return render_template('home.html', data=db_version) 

@app.route('/login', methods=['post', 'get'])
def login():
    return render_template('login.html')

@app.route('/register', methods=['post', 'get'])
def register():
    if request.method=='post':
        username = request.form.get('username')
        password = request.form.get('password')
        password1 = request.form.get('password1')

        if  username is not None and len(username) < 3:
            flash('Numele de utilizator trebuie sa fie de minim 2 caractere!', category='error')
        elif password is not None and len(password) < 5:
            flash('Parola trebuie sa fie de minim 5 caractere!', category='error')
        elif password != password1:
            flash('Cele două parole nu sunt identice!', category='error')
        else:
            flash('Cont creat cu succes!', category='success')   
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)