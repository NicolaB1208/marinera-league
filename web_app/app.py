# Searches for shows using Ajax with JSON

from cs50 import SQL
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

db = SQL("sqlite:///marinera_league_1.db")

CATEGORIES = [
    "adulto",
    "alma_de_marinera",
    "infante",
    "infantil",
    "junior",
    "juvenil",
    "master",
    "novel_a",
    "oro",
    "pre-infante",
    "senior"  
]

PHASES = [
    "eliminatoria",
    "semifinal",
    "final"
]

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search")
def search():
    q = request.args.get("q")
    if q:
        if q.startswith('single'):
            competition_results = db.execute("SELECT * FROM final_madrid_single JOIN people ON final_madrid_single.person_id = people.id WHERE category LIKE ? LIMIT 50", "%" + q + "%")
        else:
            competition_results = db.execute("SELECT * FROM final_madrid_couples JOIN couples ON final_madrid_couples.couple_id = couples.id WHERE category LIKE ? LIMIT 50", "%" + q + "%")
    else:
        competition_results = []
    return jsonify(competition_results)
