from unicodedata import category
from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from . import db
from .models import Entry, Team

from website.models import Note

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
            
    return render_template("home.html", user=current_user)

@views.route('/update')
@login_required
def update():
    return render_template("update.html", user=current_user)


@views.route('/content', methods=['GET', 'POST'])
def content():
    entries = Team.query.order_by(Team.namaTeam).all()
        
    return render_template("content.html", user=current_user, entry = entries)