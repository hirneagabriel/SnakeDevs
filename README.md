# SnakeDevs

## Instalare database windows(sqlite): <br/>
1. Descarca precompiled binaries de la https://www.sqlite.org/download.html
2. Descarca sqlite-tools-win32-x86-3370200.zip de acolo
3. Extrage fileurile in C:\sqlite (sa fie toate fileulire in rootul folderului)
4. Adauga folderul la PATH in environment variables
5. Creaza un folder db in C:\sqlite   
6. ruleza <code> sqlite3 </code> in cmd (asta verifica daca functioneaza sqlite)
Prima data cand rulezi aplicatia trebuie sa faci baza de date, asa ca mai trebuie si urmatorii pasi doar odata:
8. asigura-te ca liniile:<code>
   with app.app_context():
    db.init_db()
   </code>nu sunt comentate in app.py

9. Efeectuaza pasii de mai jos si ruleaza aplicatia odata
10. comenteaza liniile mentionate mai sus
   
## Instalare mosquitto:
https://mosquitto.org/download/ <br/>
Din cmd rulati ca admin in folderul unde s-a instalat mosquitto comanda : <code> net start mosquitto </code> <br/>
In loc de <code> flask run </code> folosim comanda <code> python app.py </code> ca sa mearga si MQTT  <br />

## Comenzi inainte de rulare: <br />
<code> set FLASK_APP=flaskr </code> <br />
<code>set FLASK_ENV=development </code><br />
<code>pip install -e . </code><br />
<code>pip install flask_socketio </code> <br />
<code>pip install flask_mqtt </code><br />
<code>pip install eventlet </code><br />

## Functionalitati
- Mod de vacanta
- Setare temperatura
- Setare lumina ambient RGB
- Timer pentru inchiderea usii
- Gestionare stoc

## Tehnologii folosite
- Flask
- MQTT
- Mosquitto
- Sqlite

## Testare
Pentru testare a fost folosit pytest. 
Comanda pentru a rula testele:
<code> python -m pytest -v </code>



