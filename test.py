from flask import Flask, render_template, url_for, request, flash, session, redirect
from datetime import timedelta
import psycopg2
import json


app = Flask(__name__)
app.secret_key = 'secretkey'
app.permanent_session_lifetime = timedelta(minutes=30)
app.config['SECRET_KEY'] = 'thisisasecretkey'

@app.route('/', methods=['post', 'get'])
@app.route('/welcome', methods=['post', 'get'])
def home():
    return render_template('home.html')


@app.route('/home', methods=['post', 'get'])
def logged_home():
    username = session['user']
    return render_template('logged_home.html',username=username) 


@app.route('/univs', methods=['post', 'get'])
def univs():
    username = session['user']
    return render_template('univs.html', username=username) 

@app.route('/favs', methods=['post', 'get'])
def favs():
    ready_list_facs = session['lista_facs']
    len_list = len(ready_list_facs)
    return render_template('favs.html', len_list=len_list, ready_list_facs=ready_list_facs, username=request.args.get('username'), username1 = session['user'] ) 

@app.route('/logout', methods=['post', 'get'])
def logout():
    session.pop('user', None)
    return redirect(url_for('login')) 

@app.route('/form_elev', methods=['post', 'get'])
def form_elev():
    if request.method == 'POST':

        session.permanent = True
        profil = request.form.get('profil')
        domeniu = request.form.getlist('domeniu')
        admitere = request.form.getlist('admitere')
        orase = request.form.getlist('orase')
        taxa = request.form.getlist('taxa')
        print(profil)
        print(domeniu)
        print(admitere)
        print(orase)
        print(taxa)

        conn = psycopg2.connect("postgresql://postgres:postgres@localhost:5432/licenta")
        crsr = conn.cursor()
        crsr1 = conn.cursor()
        crsr2 = conn.cursor()

        listdom = ['None'] * 6
        if len(domeniu) == 6:
            listdom = domeniu
        elif len(domeniu) == 5:
            listdom[:5] = domeniu
        elif len(domeniu) == 4:
            listdom[:4] = domeniu
        elif len(domeniu) == 3:
            listdom[:3] = domeniu
        elif len(domeniu) == 2:
            listdom[:2] = domeniu
        elif len(domeniu) == 1:
            listdom[:1] = domeniu
        else:
            print('n-a fost selectat nimic la domeniu')
        print(listdom)


        
        listadm = ['None'] * 2
        if len(admitere) == 2:
            listadm = admitere
        elif len(admitere) == 1:
            listadm[:1] = admitere
        else:
            print('n-a fost selectat nimic la admitere')
        print(listadm)


        listorase = ['None'] * 6
        if len(orase) == 6:
            listorase = orase
        elif len(orase) == 5:
            listorase[:5] = orase
        elif len(orase) == 4:
            listorase[:4] = orase
        elif len(orase) == 3:
            listorase[:3] = orase
        elif len(orase) == 2:
            listorase[:2] = orase
        elif len(orase) == 1:
            listorase[:1] = orase
        else:
            print('n-a fost selectat nimic la orase')
        print(listorase)


        listtaxa = ['None'] * 2
        if len(taxa) == 2:
            listtaxa = taxa
        elif len(taxa) == 1:
            listtaxa[:1] = taxa
        else:
            print('n-a fost selectat nimic la taxa')
        print(listtaxa)

        if listtaxa[1] == 'None':
            crsr.execute("SELECT distinct facName,univName,locatie,rating,duratalicenta,taxa,ultimamedie,domeniu,programestudiu FROM Facs where profilelev=%(profil)s and taxa=%(taxa)s and (domeniu~%(domeniu1)s or domeniu~%(domeniu2)s or domeniu~%(domeniu3)s or domeniu~%(domeniu4)s or domeniu~%(domeniu5)s or domeniu~%(domeniu6)s) and (locatie=%(oras1)s or locatie=%(oras2)s or locatie=%(oras3)s or locatie=%(oras4)s or locatie=%(oras5)s or locatie=%(oras6)s) and (tipAdmitere=%(admitere1)s or tipAdmitere=%(admitere2)s)", {'profil': profil, 'domeniu1': listdom[0],'domeniu2': listdom[1], 'domeniu3': listdom[2],'domeniu4': listdom[3], 'domeniu5': listdom[4],'domeniu6': listdom[5], 'admitere1': listadm[0], 'admitere2': listadm[1], 'oras1':listorase[0], 'oras2':listorase[1], 'oras3':listorase[2], 'oras4':listorase[3], 'oras5':listorase[4], 'oras6':listorase[5], 'taxa':listtaxa[0]})
            date_fac = crsr.fetchall()
        else:
            crsr2.execute("SELECT distinct facName,univName,locatie,rating,duratalicenta,taxa,ultimamedie,domeniu,programestudiu FROM Facs where profilelev=%(profil)s and (domeniu~%(domeniu1)s or domeniu~%(domeniu2)s or domeniu~%(domeniu3)s or domeniu~%(domeniu4)s or domeniu~%(domeniu5)s or domeniu~%(domeniu6)s) and (locatie=%(oras1)s or locatie=%(oras2)s or locatie=%(oras3)s or locatie=%(oras4)s or locatie=%(oras5)s or locatie=%(oras6)s) and (tipAdmitere=%(admitere1)s or tipAdmitere=%(admitere2)s)", {'profil': profil, 'domeniu1': listdom[0],'domeniu2': listdom[1], 'domeniu3': listdom[2],'domeniu4': listdom[3], 'domeniu5': listdom[4],'domeniu6': listdom[5], 'admitere1': listadm[0], 'admitere2': listadm[1], 'oras1':listorase[0], 'oras2':listorase[1], 'oras3':listorase[2], 'oras4':listorase[3], 'oras5':listorase[4], 'oras6':listorase[5]})
            date_fac = crsr2.fetchall()
        
        print(date_fac)

        if not date_fac:
            flash('Nu s-au găsit rezultate!', category='error')
            return render_template('favs.html')
        else:
            date_json = json.dumps(date_fac)
            list_facs= json.loads(date_json)
            ready_list_facs = [(x[0], x[1], x[2],x[3],x[4],x[5],x[6],x[7],x[8]) for x in list_facs]
            session['lista_facs'] = ready_list_facs
        
        len_list = len(ready_list_facs)
        
        conn.close()
        return render_template('favs.html', len_list=len_list, ready_list_facs=ready_list_facs,username=request.args.get('username'))
    return render_template('form_elev.html',username=request.args.get('username'))

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
            crsr2 = conn.cursor()
            crsr2.execute("select tip from Users where username=%(username)s and passwd=%(passwd)s", {'username': username, 'passwd': password})
            data = crsr2.fetchall()
            if data:
                tip = str(data[0][0])
                print(tip)
                if tip == 'elev':
                    if "user" not in session:
                        session['user'] = username
                    if username not in session:
                        session[username] = True
                        return redirect(url_for('form_elev', username=username))
                    return redirect(url_for('favs', username=username))    
            crsr2.close()    
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