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

@views.route('/turnament')

def turnamen():
    game = {
    "Counter Strike: Global Offensive": {
        "jadwal": "Selasa, Rabu, Kamis (April 2022 - Mei 2022)",
        "jenis": "FPS",
    },
    "Valorant": {
        "jadwal": "Jumat - Minggu (Maret 2022 - Mei 2022)",
        "jenis": "FPS", 
    },
    "PES": {
        "jadwal": "Kamis - Minggu (Mei 2022 - Juni 2022)",
        "jenis": "Football (Sports)",
    },
}
    
    query = request.args.get('query')
    data = game
    if query != None:
        data = {k:v for (k,v) in data.items() if query.lower() in k.lower()}
    return render_template("turnamen.html", data=data, query=query, datacount=len(data))
    
    