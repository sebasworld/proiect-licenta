from flask import Flask, render_template, url_for, request, flash, session, redirect
from flask_session import Session
from flask_paginate import Pagination, get_page_parameter
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

@app.route('/admin_home', methods=['post', 'get'])
def admin_home():
    return render_template('admin_home.html', username = session['user'])

@app.route('/add_fac', methods=['post', 'get'])
def add_fac():
    if request.method == 'POST':
        facName = request.form['facName']
        univName = request.form['univName']
        locatie = request.form['locatie']
        rating = request.form['rating']
        licenta = request.form['licenta']
        programeStud = request.form['programeStud']
        taxa = request.form['taxa']
        medie = request.form['medie']
        admitere = request.form['admitere']
        profil = request.form['profil']
        domeniu = request.form['domeniu']
        dific = request.form['dific']
        aspecte = request.form['aspecte']
        format1 = request.form['format']
        link_fac = request.form['linkfac']
        alumni_jobs = request.form['alumnijobs']

        conn = psycopg2.connect("postgresql://postgres:postgres@localhost:5432/licenta")
        cursor = conn.cursor()
        
        image_file = request.files['facultyPhoto']
        img_data = image_file.read()

        try:
            cursor.execute("INSERT INTO Facs (facName, univName, locatie, rating, durataLicenta, taxa, ultimaMedie, tipAdmitere, profilelev, domeniu, programestudiu,nivel_master, aspecte_domeniu_master, format_master,facimg,fac_link, alumni_jobs) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s, %s)", (facName,univName, locatie,rating, licenta ,taxa,medie,admitere,profil,domeniu,programeStud,dific, aspecte,format1,psycopg2.Binary(img_data), link_fac, alumni_jobs))
            conn.commit()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            conn.rollback()
        finally:
            conn.close()

        flash('Facultate adăugată cu succes!', category='success')
        return redirect(url_for('admin_univs'))
    return render_template('add_fac.html')

@app.route('/delete_fac', methods=['POST'])
def delete_fac():
    faculty_id = request.form['facultyId']

    conn = psycopg2.connect("postgresql://postgres:postgres@localhost:5432/licenta")
    cursor = conn.cursor()

    try:
        cursor.execute("DELETE FROM Facs WHERE facid = %s", (faculty_id,))
        conn.commit()
        flash('Facultate ștearsă cu succes!', category='success')
        return "Faculty deleted successfully", 200
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        conn.rollback()
        flash('Facultate nu a fost ștearsă!', category='error')
        return "Error deleting faculty", 500
    finally:
        conn.close()

@app.route('/modify_fac', methods=['POST', 'GET'])
def modify_fac():
    if request.method == 'POST':   
        faculty_id = request.form.get('facultyId')
        facName = request.form.get('facName')
        univName = request.form.get('univName')
        locatie = request.form.get('locatie')
        rating = request.form.get('rating')
        licenta = request.form.get('licenta')
        programeStud = request.form.get('programeStud')
        taxa = request.form.get('taxa')
        medie = request.form.get('medie')
        admitere = request.form.get('admitere')
        profil = request.form.get('profil')
        domeniu = request.form.get('domeniu')
        dific = request.form.get('dific')
        aspecte = request.form.get('aspecte')
        format1 = request.form.get('format')
        print(faculty_id)
        print(facName)
        print(dific)

        conn = psycopg2.connect("postgresql://postgres:postgres@localhost:5432/licenta")
        cursor = conn.cursor()
        try:
            cursor.execute("""
                UPDATE Facs
                SET facName = %s, univName = %s, locatie = %s,rating = %s,durataLicenta = %s,taxa = %s,ultimaMedie = %s,tipAdmitere = %s,
                profilelev = %s,domeniu = %s,programestudiu = %s,nivel_master = %s,aspecte_domeniu_master = %s,format_master = %s
                WHERE facid = %s
            """, (facName, univName, locatie,rating,licenta,taxa,medie,admitere,profil,domeniu, programeStud,dific,aspecte,format1,faculty_id))
            conn.commit()
            flash('Facultate modificată cu succes!', category='success')
            return redirect('/admin_univs') 
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)
            conn.rollback()
            flash('Eroare la modificarea facultății!', category='error')
            return redirect('/admin_univs')
        finally:
            conn.close()
    return render_template('admin_univs')

@app.route('/admin_univs', methods=['post', 'get'])
def admin_univs():
    if request.method == 'GET':
        conn = psycopg2.connect("postgresql://postgres:postgres@localhost:5432/licenta")
        crsr = conn.cursor()

        crsr.execute("SELECT distinct facName, univName,locatie,rating,duratalicenta,taxa,ultimamedie,domeniu,programestudiu,encode(facimg, 'base64') as imagine, nivel_master,aspecte_domeniu_master,format_master,facid, fac_link, alumni_jobs FROM Facs")
        date_fac = crsr.fetchall()

        if not date_fac:
            flash('Nu s-au putut accesa facultățile!', category='error')
            return render_template('admin_univs.html',date_fac=date_fac,username=session['user'])
        else:
            date_json = json.dumps(date_fac)
            list_facs= json.loads(date_json)
            ready_list_facs = [(x[0], x[1], x[2],x[3],x[4],x[5], x[6],x[7],x[8],x[9],x[10],x[11],x[12], x[13], x[14], x[15]) for x in list_facs]
            for x in list_facs:
                image_bytes = bytes(x[9], encoding='utf-8')
                decoded_image = base64.b64encode(image_bytes).decode('utf-8')
                x[9] = decoded_image

            session['ready_list_facs'] = ready_list_facs
            len_list = len(ready_list_facs)
            conn.close()
            return render_template('admin_univs.html', date_fac=date_fac, len_list=len_list, ready_list_facs=ready_list_facs,username=session['user'])
    
    return render_template('admin_univs.html', username = session['user'])

@app.route('/admin_users', methods=['post', 'get'])
def admin_users():
    if request.method == 'GET':
        conn = psycopg2.connect("postgresql://postgres:postgres@localhost:5432/licenta")
        crsr = conn.cursor()

        crsr.execute("select distinct username, tip, userid from Users")
        date_user = crsr.fetchall()

        if not date_user:
            flash('Nu s-au putut accesa datele utilizatorilor!', category='error')
            return render_template('admin_users.html',date_fac=date_user,username=session['user'])
        else:
            date_json = json.dumps(date_user)
            list_users= json.loads(date_json)
            ready_list_users = [(x[0], x[1], x[2]) for x in list_users]

            # Paginate the user list
            page = request.args.get(get_page_parameter(), type=int, default=1)
            per_page = 7
            start = (page - 1) * per_page
            end = start + per_page
            users_to_display = ready_list_users[start:end]

            # Create pagination object
            pagination = Pagination(page=page, total=len(ready_list_users), per_page=per_page)

            session['ready_list_users'] = ready_list_users
            len_list = len(ready_list_users)
            conn.close()
            return render_template('admin_users.html', date_user=date_user, len_list=len_list, ready_list_users=users_to_display, pagination = pagination, username=session['user'])
    return render_template('admin_users.html', username = session['user'])

@app.route('/home', methods=['post', 'get'])
def logged_home():
    return render_template('logged_home.html',username=session['user']) 


@app.route('/univs', methods=['post', 'get'])
def univs():
    if request.method == 'GET':
        user_type = session['tip']
        if user_type == 'elev':
            conn = psycopg2.connect("postgresql://postgres:postgres@localhost:5432/licenta")
            crsr = conn.cursor()

            crsr.execute("SELECT distinct facName, univName,locatie,rating,duratalicenta,taxa,ultimamedie,domeniu,programestudiu,encode(facimg, 'base64') as imagine, nivel_master,aspecte_domeniu_master,format_master, fac_link  FROM Facs")
            date_fac_prof_consi = crsr.fetchall()
            #print(date_fac_prof_consi)

            if not date_fac_prof_consi:
                flash('Nu s-au putut accesa facultățile!', category='error')
                return render_template('univs.html',date_fac_prof_consi=date_fac_prof_consi,username=session['user'])
            else:
                date_json = json.dumps(date_fac_prof_consi)
                list_facs= json.loads(date_json)
                ready_list_facs = [(x[0], x[1], x[2],x[3],x[4],x[5], x[6],x[7],x[8],x[9],x[10],x[11],x[12], x[13]) for x in list_facs]
                for x in list_facs:
                    image_bytes = bytes(x[9], encoding='utf-8')
                    decoded_image = base64.b64encode(image_bytes).decode('utf-8')
                    x[9] = decoded_image

                session['ready_list_facs_prof_cons'] = ready_list_facs

                len_list = len(ready_list_facs)
                conn.close()
                return render_template('univs.html', usertype = user_type,date_fac_prof_consi=date_fac_prof_consi, len_list_prof_cons=len_list, ready_list_facs_prof_cons=ready_list_facs,username=session['user'])
        elif user_type == 'student' or user_type == 'alumni':
            conn = psycopg2.connect("postgresql://postgres:postgres@localhost:5432/licenta")
            crsr = conn.cursor()

            crsr.execute("SELECT distinct facName, univName,locatie,encode(facimg, 'base64') as imagine, nivel_master,aspecte_domeniu_master,format_master, fac_link, alumni_jobs FROM Facs")
            date_fac_prof_consi = crsr.fetchall()
            #print(date_fac_prof_consi)

            if not date_fac_prof_consi:
                flash('Nu s-au putut accesa facultățile!', category='error')
                return render_template('univs.html',date_fac_prof_consi=date_fac_prof_consi,username=session['user'])
            else:
                date_json = json.dumps(date_fac_prof_consi)
                list_facs= json.loads(date_json)
                ready_list_facs = [(x[0], x[1], x[2],x[3],x[4],x[5], x[6], x[7], x[8]) for x in list_facs]
                for x in list_facs:
                    image_bytes = bytes(x[3], encoding='utf-8')
                    decoded_image = base64.b64encode(image_bytes).decode('utf-8')
                    x[3] = decoded_image

                session['ready_list_facs_prof_cons'] = ready_list_facs

                len_list = len(ready_list_facs)
                conn.close()
                return render_template('univs.html', usertype = user_type, date_fac_prof_consi=date_fac_prof_consi, len_list_prof_cons=len_list, ready_list_facs_prof_cons=ready_list_facs,username=session['user'])
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

        crsr.execute("SELECT distinct facName,univName,locatie,encode(facimg, 'base64') as imagine,nivel_master,aspecte_domeniu_master,format_master, fac_link FROM Facs where domeniu~%(domeniu)s and (aspecte_domeniu_master~%(aspecte1)s or aspecte_domeniu_master~%(aspecte2)s or aspecte_domeniu_master~%(aspecte3)s or aspecte_domeniu_master~%(aspecte4)s or aspecte_domeniu_master~%(aspecte5)s or aspecte_domeniu_master~%(aspecte6)s or aspecte_domeniu_master~%(aspecte7)s or aspecte_domeniu_master~%(aspecte8)s or aspecte_domeniu_master~%(aspecte9)s or aspecte_domeniu_master~%(aspecte10)s) and (locatie=%(oras1)s or locatie=%(oras2)s or locatie=%(oras3)s or locatie=%(oras4)s or locatie=%(oras5)s or locatie=%(oras6)s) and (nivel_master=%(dific1)s or nivel_master=%(dific2)s or nivel_master=%(dific3)s or nivel_master=%(dific4)s) and (format_master=%(format1)s or format_master=%(format2)s)", {'domeniu': domeniu, 'aspecte1': listaspecte[0],'aspecte2': listaspecte[1], 'aspecte3': listaspecte[2],'aspecte4': listaspecte[3], 'aspecte5': listaspecte[4],'aspecte6': listaspecte[5], 'aspecte7': listaspecte[6],'aspecte8': listaspecte[7], 'aspecte9': listaspecte[8],'aspecte10': listaspecte[9], 'oras1':listorase[0], 'oras2':listorase[1], 'oras3':listorase[2], 'oras4':listorase[3], 'oras5':listorase[4], 'oras6':listorase[5], 'dific1':listdif[0], 'dific2':listdif[1], 'dific3':listdif[2],'dific4':listdif[3],'format1':listformat[0],'format2':listformat[1]})
        date_fac_student = crsr.fetchall()
        #print(date_fac_student)

        if not date_fac_student:
            flash('Nu s-au găsit rezultate!', category='error')
            return redirect(url_for('favs',date_fac_student=date_fac_student,username=session['user']))
        else:
            date_json = json.dumps(date_fac_student)
            list_facs= json.loads(date_json)
            ready_list_facs = [(x[0], x[1], x[2],x[3],x[4],x[5],x[6], x[7]) for x in list_facs]
            for x in list_facs:
                image_bytes = bytes(x[3], encoding='utf-8')
                decoded_image = base64.b64encode(image_bytes).decode('utf-8')
                x[3] = decoded_image

            user_type = 'student'
            user_id = session['userid']

            if user_type not in session:
                session[user_type] = {}
            session[user_type][user_id] = ready_list_facs
            
            conn.close()
            return redirect(url_for('favs'))

    return render_template('form_student.html',username=session['user'])


from flask import request, jsonify, session

@app.route('/add_to_favorites', methods=['POST'])
def add_to_favorites():
    # Get the index from the request JSON data
    index = int(request.json.get('index'))

    # Check if the index is valid
    if index is None:
        return jsonify(message='Invalid index.'), 400

    # Get the selected panel data from the "univs" page
    selected_panel = session['ready_list_facs_prof_cons'][index]

    # Get the user type and user ID from the session
    user_type = session.get('tip')
    user_id = session.get('userid')

    # Check if user type and user ID are present in the session
    if not user_type or not user_id:
        return jsonify(message='User not authenticated.'), 401

    # Check the user type and update the session accordingly
    if user_type == 'student':
        session.setdefault('student', {}).setdefault(user_id, []).append(selected_panel)
        flash("Facultatea a fost adăugată cu succes la Favorite!", category='success')
    elif user_type == 'elev':
        session.setdefault('elev', {}).setdefault(user_id, []).append(selected_panel)
        flash("Facultatea a fost adăugată cu succes la Favorite!", category='success')
    else:
        return jsonify(message='Invalid user type.'), 400
    return redirect(url_for('favs'))


@app.route('/remove_panel', methods=['POST'])
def remove_panel():
    user_type = request.form.get('userType')
    index_str = request.form.get('index')

    if user_type is None or index_str is None:
        return 'Invalid request data.'

    try:
        index = int(index_str)
    except (ValueError, TypeError):
        return 'Invalid index value.'

    # Remove the panel data from the session based on the user type and index
    if user_type == 'elev' and session.get('elev'):
        elev_data = session['elev'].get(session['userid'])
        if elev_data and 0 <= index < len(elev_data):
            del elev_data[index]
            flash("Facultate ștearsă cu succes!", category='success')
        else:
            return 'User data not found in session.'
    elif user_type == 'student' and session.get('student'):
        student_data = session['student'].get(session['userid'])
        if student_data and 0 <= index < len(student_data):
            del student_data[index]
            flash("Facultate ștearsă cu succes!", category='success')
        else:
            return 'User data not found in session.'
    else:
        return 'Invalid user type.'

    return redirect(url_for('favs'))
 

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
            crsr.execute("SELECT distinct facName,univName,locatie,rating,duratalicenta,taxa,ultimamedie,domeniu,programestudiu,encode(facimg, 'base64') as imagine, fac_link FROM Facs where profilelev=%(profil)s and taxa=%(taxa)s and (domeniu~%(domeniu1)s or domeniu~%(domeniu2)s or domeniu~%(domeniu3)s or domeniu~%(domeniu4)s or domeniu~%(domeniu5)s or domeniu~%(domeniu6)s) and (locatie=%(oras1)s or locatie=%(oras2)s or locatie=%(oras3)s or locatie=%(oras4)s or locatie=%(oras5)s or locatie=%(oras6)s) and (tipAdmitere=%(admitere1)s or tipAdmitere=%(admitere2)s)", {'profil': profil, 'domeniu1': listdom[0],'domeniu2': listdom[1], 'domeniu3': listdom[2],'domeniu4': listdom[3], 'domeniu5': listdom[4],'domeniu6': listdom[5], 'admitere1': listadm[0], 'admitere2': listadm[1], 'oras1':listorase[0], 'oras2':listorase[1], 'oras3':listorase[2], 'oras4':listorase[3], 'oras5':listorase[4], 'oras6':listorase[5], 'taxa':listtaxa[0]})
            date_fac = crsr.fetchall()
        else:
            crsr2.execute("SELECT distinct facName,univName,locatie,rating,duratalicenta,taxa,ultimamedie,domeniu,programestudiu,encode(facimg, 'base64') as imagine, fac_link FROM Facs where profilelev=%(profil)s and (domeniu~%(domeniu1)s or domeniu~%(domeniu2)s or domeniu~%(domeniu3)s or domeniu~%(domeniu4)s or domeniu~%(domeniu5)s or domeniu~%(domeniu6)s) and (locatie=%(oras1)s or locatie=%(oras2)s or locatie=%(oras3)s or locatie=%(oras4)s or locatie=%(oras5)s or locatie=%(oras6)s) and (tipAdmitere=%(admitere1)s or tipAdmitere=%(admitere2)s)", {'profil': profil, 'domeniu1': listdom[0],'domeniu2': listdom[1], 'domeniu3': listdom[2],'domeniu4': listdom[3], 'domeniu5': listdom[4],'domeniu6': listdom[5], 'admitere1': listadm[0], 'admitere2': listadm[1], 'oras1':listorase[0], 'oras2':listorase[1], 'oras3':listorase[2], 'oras4':listorase[3], 'oras5':listorase[4], 'oras6':listorase[5]})
            date_fac = crsr2.fetchall()
        
        #print(date_fac)

        if not date_fac:
            flash('Nu s-au găsit rezultate!', category='error')
            return redirect(url_for('favs',date_fac=date_fac,username=session['user']))
        else:
            date_json = json.dumps(date_fac)
            list_facs= json.loads(date_json)
            ready_list_facs = [(x[0], x[1], x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10]) for x in list_facs]
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
        if username == 'Admin' and password == 'admin':
            session['user'] = username
            return redirect(url_for('admin_home'))
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
                elif tip == 'alumni':
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
            flash('Cont creat cu succes! Puteți să vă logați!', category='success')
            crsr = conn.cursor()
            crsr.execute("insert into Users(username,tip,passwd) VALUES(%(username)s, %(tip)s , %(passwd)s)", {'username': username, 'tip': user_type, 'passwd': password}) 
            conn.commit()
            crsr.close()
            conn.close()
            return redirect(url_for('login'))
    return render_template('register.html')





if __name__ == '__main__':
    app.run(debug=True)