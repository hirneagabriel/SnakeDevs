# SnakeDevs

Instalare database windows(sqlite): <br/>
1. Descarca precompiled binaries de la https://www.sqlite.org/download.html
2. Descarca sqlite-tools-win32-x86-3370200.zip de acolo
3. Extrage fileurile in C:\sqlite (sa fie toate fileulire in rootul folderului)
4. Adauga folderul la PATH in environment variables
5. Creaza un folder db in C:\sqlite   
6. ruleza sqlite3 in cmd (asta verifica daca functioneaza sqlite)
Prima data cand rulezi aplicatia trebuie sa faci baza de date, asa ca mai trebuie si urmatorii pasi doar odata:
8. asigura-te ca liniile:
<code>
   with app.app_context():
    db.init_db()
   </code> nu sunt comentate in app.py
9. Efeectuaza pasii de mai jos si ruleaza aplicatia odata
10. comenteaza liniile mentionate mai sus
   


Comenzi inainte de rulare: <br />
set FLASK_APP=flaskr <br />
set FLASK_ENV=development<br />
pip install -e .<br />
pip install flask_socketio <br />
pip install flask_mqtt <br />
pip install eventlet <br />

Instalati mosquitto: https://mosquitto.org/download/
Din cmd rulati ca admin in folderul unde s-a instalat mosquitto comanda : net start mosquitto
In loc de flask run folosim python app.py ca sa mearga si MQTT  <br />




