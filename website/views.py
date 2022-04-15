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

@views.route('/update')
@login_required
def update():
    return render_template("update.html", user=current_user)

@views.route('/content')
@login_required
def content():
    return render_template("content.html", user=current_user)