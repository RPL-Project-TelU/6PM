from unicodedata import category
from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from . import db

from website.models import Note

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        
        if len(note) < 1:
            flash('Note is to short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
            
    return render_template("home.html", user=current_user)

@views.route('/profile')
@login_required
def profile():
    return render_template("profile.html", user=current_user)

class DataUtil:
    #membuat class datautil
    def __init__(self):
        #table driven
        #digunakan untuk pencarian turnamen bedasarkan nama game
        self.__game1 = {
            "Counter Strike: Global Offensive": {
                "jadwal": "Selasa, Rabu, Kamis (April 2022 - Mei 2022)",
                "jenis": "FPS",
                "gambar": "csgo.jpg"
            },
            "Valorant": {
                "jadwal": "Jumat - Minggu (Maret 2022 - Mei 2022)",
                "jenis": "FPS",
                "gambar": "valorant.jpg"
            },
            
            "Dota 2": {
                "jadwal": "Senin, Sabtu, Minggu (April 2022 - Juni 2022)",
                "jenis": "MOBA",
                "gambar": "dota2.jpeg"
            },
            "League of Legends": {
                "jadwal": "Senin - Rabu (Februari 2022 - April 2022)",
                "jenis": "MOBA",
                "gambar": "lol.jpg"
            },
           
            "PUBG Battlegrounds": {
                "jadwal": "Jumat, Minggu (Mei 2022 - Juli 2022)",
                "jenis": "Survival - TPS",
                "gambar": "pubg.jpg"
            },
            "Fortnite": {
                "jadwal": "Jumat - Minggu (April 2022 - Juli 2022)",
                "jenis": "Survival - TPS",
                "gambar": "fortnite.jpg"
            },
            
            "Apex Legends": {
                "jadwal": "Selasa - Kamis (April 2022 - Mei 2022)",
                "jenis": "Survival",
                "gambar": "apex.jpg"
            },
            
            "Call of Duty Cold War": {
                "jadwal": "Sabtu, Minggu (Juli 2022 - September 2022)",
                "jenis": "FPS",
                "gambar": "cod.jpg"
            },
            "PES": {
                "jadwal": "Kamis - Minggu (Mei 2022 - Juni 2022)",
                "jenis": "Football (Sports)",
                "gambar": "pes.jpg"
            },
        }

    def getGame(self, query):
        tmp = self.__game
        if query != None:
            tmp = {k:v for (k,v) in tmp.items() if query.lower() in k.lower()}
    # fungsi yang kanan biar mencari game lebih singkat
        return tmp

class DataUtilFactory:
    def create(self):
        return DataUtil()