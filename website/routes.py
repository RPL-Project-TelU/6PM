from turtle import title
from unicodedata import name
from flask import render_template, request, redirect
from app import app, db
from app.models import Entry
from . import db

jedi = "of the jedi"

@app.route('/')
@app.route('/index')
def index():
    entries = Entry.query.all()
    return render_template('content.html', entries=entries)

@app.route('/content', methods=['POST'])
def content():
    if request.method == 'POST':
        form = request.form
        namaTeam = form.get('Nama Team')
        desc = form.get('description')
        game = form.get('game')
        if not namaTeam or desc:
            entry = Entry(NamaTeam = namaTeam, description = desc, game = game)
            db.session.add(entry)
            db.session.commit()
            return redirect('/')

    return "of the jedi"

@app.route('/update/<int:id>')
def updateRoute(id):
    if not id or id != 0:
        entry = Entry.query.get(id)
        if entry:
            return render_template('update.html', entry=entry)

    return "of the jedi"

@app.route('/update', methods=['POST'])
def update():
    if not id or id != 0:
        entry = Entry.query.get(id)
        if entry:
            db.session.delete(entry)
            db.session.commit()
        return redirect('/')

    return "of the jedi"



@app.route('/delete/<int:id>')
def delete(id):
    if not id or id != 0:
        entry = Entry.query.get(id)
        if entry:
            db.session.delete(entry)
            db.session.commit()
        return redirect('/')

    return "of the jedi"

@app.route('/turn/<int:id>')
def turn(id):
    if not id or id != 0:
        entry = Entry.query.get(id)
        if entry:
            entry.status = not entry.status
            db.session.commit()
        return redirect('/')

    return "of the jedi"
