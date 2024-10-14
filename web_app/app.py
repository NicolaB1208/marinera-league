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
    "senior",
    "single_a",
    "single_b",
    "single_c"  
]

PHASES = [
    "eliminatoria",
    "semifinal",
    "final"
]

COMPETITIONS = [
    "madrid"
]

@app.route("/")
def index():
    return render_template("index.html", categories = CATEGORIES, competitions = COMPETITIONS, phases = PHASES)


@app.route("/search")
def search():
    category = request.args.get("q")
    phase = request.args.get("phase")

    valid_tables = ["final_madrid_single", "final_madrid_couples","semifinal_madrid_single", "semifinal_madrid_couples",
    "eliminatoria_madrid_single", "eliminatoria_madrid_couples"]

    if category.startswith('single'):
        ending = 'single'
    else:
        ending = 'couples'
    
    table_name = phase + '_madrid_' + ending

    if table_name in valid_tables:
        if category.startswith('single'):
            query = f"SELECT * FROM {table_name} JOIN people ON {table_name}.person_id = people.id WHERE category = ? ORDER BY total_score DESC"
        else:
            query = f"SELECT * FROM {table_name} JOIN couples ON {table_name}.couple_id = couples.id WHERE category = ? ORDER BY total_score DESC"
        competition_results = db.execute(query, (category))
    else:
        competition_results = []
    return jsonify(competition_results)



