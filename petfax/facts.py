import json
from flask import Blueprint, render_template, request, redirect

bp_facts = Blueprint("facts", __name__, url_prefix="/facts")

@bp_facts.route("/", methods=["GET", "POST"])
def index():
    
    if request.method == "POST":
        print (request.form)
        # return render_template("facts.html")
        return redirect('/facts')
    return render_template("facts/index.html")

@bp_facts.route("/new")
def facts_new():
    return render_template("new_fact.html")