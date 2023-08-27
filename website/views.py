from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        note = request.form.get('note')#Gets the note from the HTML 

        if len(note) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_note = Note(data=note, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_note) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/Underweight')
def underweight():
    return render_template("Underweight.html", user=current_user)

@views.route('/Overweight')
def overweight():
    return render_template("Overweight.html", user=current_user)

@views.route('/Wasting')
def Wasting():
    return render_template("Wasting.html", user=current_user)

@views.route('/Severewasting')
def Severewasting():
    return render_template("Severewasting.html", user=current_user)

@views.route('/Stunting')
def Stunting():
    return render_template("Stunting.html", user=current_user)

@views.route('/ABM')
def ABM():
    return render_template("ABM.html", user=current_user)

@views.route('/AboutUs')
def AboutUs():
    return render_template("AboutUs.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():  
    note = json.loads(request.data) # this function expects a JSON from the INDEX.js file 
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})