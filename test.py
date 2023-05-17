from flask import Flask, render_template, url_for, request, flash, session, redirect
from flask_session import Session
from redis import Redis
from datetime import timedelta
import psycopg2
import json
import base64


app = Flask(__name__)
app.secret_key = 'secretkey'

app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_REDIS'] = Redis(host='localhost', port=6379)
Session(app)

app.permanent_session_lifetime = timedelta(days=1)


@app.route('/', methods=['post', 'get'])
@app.route('/welcome', methods=['post', 'get'])
def home():
    return render_template('home.html')

@app.route('/home', methods=['post', 'get'])
def logged_home():
    return render_template('logged_home.html',username=session['user']) 


@app.route('/univs', methods=['post', 'get'])
def univs():
    if request.method == 'GET':
        conn = psycopg2.connect("postgresql://postgres:postgres@localhost:5432/licenta")
        crsr = conn.cursor()

        crsr.execute("SELECT distinct univName,facName,locatie,rating,duratalicenta,taxa,ultimamedie,domeniu,programestudiu,nivel_master,aspecte_domeniu_master,format_master,encode(facimg, 'base64') as imagine FROM Facs")
        date_fac_prof_consi = crsr.fetchall()
        #print(date_fac_prof_consi)

        if not date_fac_prof_consi:
            flash('Nu s-au putut accesa facultățile!', category='error')
            return render_template('univs.html',date_fac_prof_consi=date_fac_prof_consi,username=session['user'])
        else:
            date_json = json.dumps(date_fac_prof_consi)
            list_facs= json.loads(date_json)
            ready_list_facs = [(x[0], x[1], x[2],x[3],x[4],x[5], x[6],x[7],x[8],x[9],x[10],x[11],x[12]) for x in list_facs]
            for x in list_facs:
                image_bytes = bytes(x[12], encoding='utf-8')
                decoded_image = base64.b64encode(image_bytes).decode('utf-8')
                x[12] = decoded_image

            len_list = len(ready_list_facs)
            conn.close()
            return render_template('univs.html', date_fac_prof_consi=date_fac_prof_consi, len_list_prof_cons=len_list, ready_list_facs_prof_cons=ready_list_facs,username=session['user'])
    return render_template('univs.html', username = session['user'])



@app.route('/favs', methods=['post', 'get'])
def favs():
    if 'user' in session:
        user_type = session['tip']
        user_id = session['userid']

        if user_type == 'student':
            if user_id in session.get('student', {}):
                student_data = session['student'][user_id]
                return render_template('favs.html', usertype = user_type,ready_list_facs_student = student_data, lungime = len(student_data), username = session['user'])
                
        elif user_type == 'elev':
            if user_id in session.get('elev', {}):
                elev_data = session['elev'][user_id]
                return render_template('favs.html',usertype =user_type, ready_list_facs = elev_data, lungime = len(elev_data), username=session['user'])
             
    return render_template('favs.html', username = session['user'])


@app.route('/logout', methods=['post', 'get'])
def logout():
    session.pop('user', None)
    return redirect(url_for('login')) 

@app.route('/form_student', methods=['post', 'get'])
def form_student():
    if request.method == 'POST':
        session.permanent = True
        domeniu = request.form.get('domeniu')
        aspecte = request.form.getlist('aspecte')
        dific = request.form.getlist('dific')
        orase = request.form.getlist('orase')
        formatul = request.form.getlist('format')
        print(domeniu)
        print(aspecte)
        print(dific)
        print(orase)
        print(formatul)


        conn = psycopg2.connect("postgresql://postgres:postgres@localhost:5432/licenta")
        crsr = conn.cursor()

        listaspecte = ['None'] * 10
        if len(aspecte) == 10:
            listaspecte = aspecte
        elif len(aspecte) == 9:
            listaspecte[:9] = aspecte
        elif len(aspecte) == 8:
            listaspecte[:8] = aspecte
        elif len(aspecte) == 7:
            listaspecte[:7] = aspecte
        elif len(aspecte) == 6:
            listaspecte[:6] = aspecte
        elif len(aspecte) == 5:
            listaspecte[:5] = aspecte
        elif len(aspecte) == 4:
            listaspecte[:4] = aspecte
        elif len(aspecte) == 3:
            listaspecte[:3] = aspecte
        elif len(aspecte) == 2:
            listaspecte[:2] = aspecte
        elif len(aspecte) == 1:
            listaspecte[:1] = aspecte
        else:
            print('n-a fost selectat nimic la aspecte')
        print(listaspecte)


        listdif = ['None'] * 4
        if len(dific) == 4:
            listdif = dific
        elif len(dific) == 3:
            listdif[:3] = dific
        elif len(dific) == 2:
            listdif[:2] = dific
        elif len(dific) == 1:
            listdif[:1] = dific
        else:
            print('n-a fost selectat nimic la dificultate')
        print(listdif)


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


        listformat = ['None'] * 2
        if len(formatul) == 2:
            listformat = formatul
        elif len(formatul) == 1:
            listformat[:1] = formatul
        else:
            print('n-a fost selectat nimic la format')
        print(listformat)

        crsr.execute("SELECT distinct facName,univName,locatie,nivel_master,aspecte_domeniu_master,format_master,encode(facimg, 'base64') as imagine FROM Facs where domeniu~%(domeniu)s and (aspecte_domeniu_master~%(aspecte1)s or aspecte_domeniu_master~%(aspecte2)s or aspecte_domeniu_master~%(aspecte3)s or aspecte_domeniu_master~%(aspecte4)s or aspecte_domeniu_master~%(aspecte5)s or aspecte_domeniu_master~%(aspecte6)s or aspecte_domeniu_master~%(aspecte7)s or aspecte_domeniu_master~%(aspecte8)s or aspecte_domeniu_master~%(aspecte9)s or aspecte_domeniu_master~%(aspecte10)s) and (locatie=%(oras1)s or locatie=%(oras2)s or locatie=%(oras3)s or locatie=%(oras4)s or locatie=%(oras5)s or locatie=%(oras6)s) and (nivel_master=%(dific1)s or nivel_master=%(dific2)s or nivel_master=%(dific3)s or nivel_master=%(dific4)s) and (format_master=%(format1)s or format_master=%(format2)s)", {'domeniu': domeniu, 'aspecte1': listaspecte[0],'aspecte2': listaspecte[1], 'aspecte3': listaspecte[2],'aspecte4': listaspecte[3], 'aspecte5': listaspecte[4],'aspecte6': listaspecte[5], 'aspecte7': listaspecte[6],'aspecte8': listaspecte[7], 'aspecte9': listaspecte[8],'aspecte10': listaspecte[9], 'oras1':listorase[0], 'oras2':listorase[1], 'oras3':listorase[2], 'oras4':listorase[3], 'oras5':listorase[4], 'oras6':listorase[5], 'dific1':listdif[0], 'dific2':listdif[1], 'dific3':listdif[2],'dific4':listdif[3],'format1':listformat[0],'format2':listformat[1]})
        date_fac_student = crsr.fetchall()
        #print(date_fac_student)

        if not date_fac_student:
            flash('Nu s-au găsit rezultate!', category='error')
            return redirect(url_for('favs',date_fac_student=date_fac_student,username=session['user']))
        else:
            date_json = json.dumps(date_fac_student)
            list_facs= json.loads(date_json)
            ready_list_facs = [(x[0], x[1], x[2],x[3],x[4],x[5],x[6]) for x in list_facs]
            for x in list_facs:
                image_bytes = bytes(x[6], encoding='utf-8')
                decoded_image = base64.b64encode(image_bytes).decode('utf-8')
                x[6] = decoded_image

            user_type = 'student'
            user_id = session['userid']

            if user_type not in session:
                session[user_type] = {}
            session[user_type][user_id] = ready_list_facs
            
            conn.close()
            return redirect(url_for('favs'))

    return render_template('form_student.html',username=session['user'])




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
            crsr.execute("SELECT distinct facName,univName,locatie,rating,duratalicenta,taxa,ultimamedie,domeniu,programestudiu,encode(facimg, 'base64') as imagine FROM Facs where profilelev=%(profil)s and taxa=%(taxa)s and (domeniu~%(domeniu1)s or domeniu~%(domeniu2)s or domeniu~%(domeniu3)s or domeniu~%(domeniu4)s or domeniu~%(domeniu5)s or domeniu~%(domeniu6)s) and (locatie=%(oras1)s or locatie=%(oras2)s or locatie=%(oras3)s or locatie=%(oras4)s or locatie=%(oras5)s or locatie=%(oras6)s) and (tipAdmitere=%(admitere1)s or tipAdmitere=%(admitere2)s)", {'profil': profil, 'domeniu1': listdom[0],'domeniu2': listdom[1], 'domeniu3': listdom[2],'domeniu4': listdom[3], 'domeniu5': listdom[4],'domeniu6': listdom[5], 'admitere1': listadm[0], 'admitere2': listadm[1], 'oras1':listorase[0], 'oras2':listorase[1], 'oras3':listorase[2], 'oras4':listorase[3], 'oras5':listorase[4], 'oras6':listorase[5], 'taxa':listtaxa[0]})
            date_fac = crsr.fetchall()
        else:
            crsr2.execute("SELECT distinct facName,univName,locatie,rating,duratalicenta,taxa,ultimamedie,domeniu,programestudiu,encode(facimg, 'base64') as imagine FROM Facs where profilelev=%(profil)s and (domeniu~%(domeniu1)s or domeniu~%(domeniu2)s or domeniu~%(domeniu3)s or domeniu~%(domeniu4)s or domeniu~%(domeniu5)s or domeniu~%(domeniu6)s) and (locatie=%(oras1)s or locatie=%(oras2)s or locatie=%(oras3)s or locatie=%(oras4)s or locatie=%(oras5)s or locatie=%(oras6)s) and (tipAdmitere=%(admitere1)s or tipAdmitere=%(admitere2)s)", {'profil': profil, 'domeniu1': listdom[0],'domeniu2': listdom[1], 'domeniu3': listdom[2],'domeniu4': listdom[3], 'domeniu5': listdom[4],'domeniu6': listdom[5], 'admitere1': listadm[0], 'admitere2': listadm[1], 'oras1':listorase[0], 'oras2':listorase[1], 'oras3':listorase[2], 'oras4':listorase[3], 'oras5':listorase[4], 'oras6':listorase[5]})
            date_fac = crsr2.fetchall()
        
        #print(date_fac)

        if not date_fac:
            flash('Nu s-au găsit rezultate!', category='error')
            return redirect(url_for('favs',date_fac=date_fac,username=session['user']))
        else:
            date_json = json.dumps(date_fac)
            list_facs= json.loads(date_json)
            ready_list_facs = [(x[0], x[1], x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9]) for x in list_facs]
            for x in list_facs:
                image_bytes = bytes(x[9], encoding='utf-8')
                decoded_image = base64.b64encode(image_bytes).decode('utf-8')
                x[9] = decoded_image
                
            user_type = 'elev'
            user_id = session['userid']

            if user_type not in session:
                session[user_type] = {}
            session[user_type][user_id] = ready_list_facs

            conn.close()
            return redirect(url_for('favs'))
    return render_template('form_elev.html',username=session['user'])

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
            crsr2.execute("select tip,userid,random_string from Users where username=%(username)s and passwd=%(passwd)s", {'username': username, 'passwd': password})
            data = crsr2.fetchall()
            if data:
                tip = str(data[0][0])
                userid = str(data[0][1])
                print(tip)
                print(userid)
                if tip == 'elev':
                    if "user" not in session:
                        session['user'] = username
                        session['userid'] = userid   
                        session['tip'] = tip                      
                    if username not in session:
                        session[username] = True
                        return redirect(url_for('form_elev'))
                    return redirect(url_for('favs'))  
                elif tip == 'student':
                    if "user" not in session:
                        session['user'] = username
                        session['userid'] = userid
                        session['tip'] = tip 
                    if username not in session:
                        session[username] = True
                        return redirect(url_for('form_student'))
                    return redirect(url_for('favs'))   
                elif tip == 'profesor' or tip == 'consilier cariera':
                    if "user" not in session:
                        session['user'] = username
                        session['tip'] = tip 
                        session['userid'] = userid
                    if username not in session:
                        session[username] = True
                        return redirect(url_for('univs'))
                    return redirect(url_for('univs'))
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