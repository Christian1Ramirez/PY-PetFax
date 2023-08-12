import json
from flask import Blueprint, render_template, request

bp_facts = Blueprint("facts", __name__, url_prefix="/facts")

@bp_facts.route("/", methods=["POST"])
def index():
    print (request.form)
    # return render_template("facts.html")
    return "submitted fact"

@bp_facts.route("/new")
def facts_new():
    return render_template("new_fact.html")