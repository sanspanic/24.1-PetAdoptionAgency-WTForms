from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///petadoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'qwoidqwidubqwduqw'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def home_page(): 
    """homepage showing all pets"""

    pets = Pet.query.all()

    return render_template('index.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet(): 
    """GET route shows add new pet form, POST route validates form"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        age = form.age.data
        notes = form.notes.data
        photo_url = form.photo_url.data

        new_pet = Pet(name=name, species=species, age=age, photo_url=photo_url, notes=notes)
        db.session.add(new_pet)
        db.session.commit()

        flash(f"Added {name} the {species}, age {age}")
        return redirect("/")

    else:
        return render_template("add.html", form=form)




    return render_template('add.html', form=form)

