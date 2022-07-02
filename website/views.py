from textwrap import indent
from tkinter import N
from unicodedata import category
from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from . import db
import json

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

@views.route('/team', methods=['GET', 'POST'])
@login_required
def team():
    if request.method == 'POST':
        Games = request.form.getlist('game')
        Platform = request.form.getlist('platform')
        tteam = request.form.get('name')
        Description = request.form.get('deskripsi')
  
        with open("a+") as file:
            data = {}
            data['Team'] = []
            data['Team'].append({
                "Game": Games,
                "Platform": Platform, 
                "Team Name": tteam,
                "Description": Description
            })
            file.write(json.dumps(data, indent=2))
            file.write("\n")
    return render_template("team.html", user=current_user)