import json

from flask import Blueprint, render_template, request, redirect

bp = Blueprint(
    "pet",
    __name__,
    url_prefix="/pets",
)

@bp.route('/')
def index():
    pets = json.load(open('pets.json'))
    return render_template(
        'index.html',
        pets=pets
    )

@bp.route('/<int:index>')
def show(index):
    pets = json.load(open('pets.json'))
    pet = pets[index]
    return render_template('show.html', pet=pet)

@bp.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == "POST":
        return redirect(url_for('pet.new'))
    return render_template('new_fact.html')
