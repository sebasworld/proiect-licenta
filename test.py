from flask import Flask, render_template, url_for, request, flash
from flask_login import UserMixin
import psycopg2

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisasecretkey'


@app.route('/home', methods=['post', 'get'])
def home():
    conn = psycopg2.connect("postgresql://postgres:postgres@localhost:5432/licenta")
    crsr = conn.cursor()
    crsr.execute('SELECT username from Users')
    creds = crsr.fetchall()
    return render_template('home.html', data=creds) 

@app.route('/login', methods=['post', 'get'])
def login():
    if request.method=='POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(username)
        print(password)
        conn = psycopg2.connect("postgresql://postgres:postgres@localhost:5432/licenta")
        crsr = conn.cursor()
        crsr.execute("select username,passwd from Users where username=%(username)s and passwd=%(passwd)s", {'username': username, 'passwd': password})
        if not username and not password:
            flash('Trebuie să completați câmpurile!', category='error')
        elif not username and password:
            flash('Trebuie să introduceți numele de utilizator!', category='error')
        elif not password and username:
            flash('Trebuie să introduceți parola!', category='error')
        elif crsr.fetchone() is None:
            flash('Credențialele introduse nu corecte!', category='error')     
        else:
            #flash('V-ați logat cu succes!', category='success')
            return render_template('home.html')
        crsr.close()
        conn.close()   
    return render_template('login.html')

@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method=='POST':
        conn = psycopg2.connect("postgresql://postgres:postgres@localhost:5432/licenta")
        username = request.form.get('username')
        password = request.form.get('password')
        password1 = request.form.get('password1')
        user_type = request.form.get('user-type')
        print(username)
        print(password)
        print(password1)
        print(user_type)
        crsr2 = conn.cursor()
        crsr2.execute("select username from Users where username=%(username)s", {'username': username}) 
        if  username is not None and len(username) < 3:
            flash('Numele de utilizator trebuie sa fie de minim 2 caractere!', category='error')
        elif crsr2.fetchone() is not None:
            flash('Numele de utilizator introdus este deja existent!', category='error')
        elif password is not None and len(password) < 5:
            flash('Parola trebuie sa fie de minim 5 caractere!', category='error')
        elif password != password1:
            flash('Cele două parole nu sunt identice!', category='error')
        elif user_type is None:
            flash('Este obligatoriu să alegeți un tip de utilizator!', category='error')
        else:
            flash('Cont creat cu succes! Accesați pagina de logare.', category='success')
            crsr = conn.cursor()
            crsr.execute("insert into Users(username,tip,passwd) VALUES(%(username)s, %(tip)s , %(passwd)s)", {'username': username, 'tip': user_type, 'passwd': password}) 
            conn.commit()
            crsr.close()
            conn.close()
    return render_template('register.html')





if __name__ == '__main__':
    app.run(debug=True)