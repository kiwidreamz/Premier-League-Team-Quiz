import os

from cs50 import SQL
from flask import Flask, render_template, request
from flask_session import Session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///teams.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
def index():
    """Show landing Page"""

    # Reset database
    db.execute("UPDATE teams SET points = 0")

    return render_template("index.html")

@app.route("/quiz")
def quiz():
    """Show quiz page"""

    # Reset database
    db.execute("UPDATE teams SET points = 0")

    return render_template("quiz.html")


@app.route("/results", methods=["GET", "POST"])
def results():
    """Show which team you should support"""

    # Create a big array with the id of each team that should get points based on selected button
    data = request.form.to_dict()
    #print(data)
    results_figures = []
    for key in data:
        chunks = data[key].split(',')
        results_figures = results_figures + chunks

    print(results_figures)

    # Iterate through array and update points score in database
    for number in results_figures:
        db.execute("UPDATE teams SET points = points + 20 WHERE id = ?", number)

    # Get team with most points
    winner_list = db.execute("SELECT name FROM teams WHERE points = (SELECT MAX(points) FROM teams)")
    winner_dict = winner_list[0]
    winner = winner_dict.get("name")
    print(winner)

    # Get description from database
    desc_list = db.execute("SELECT desc FROM descriptions WHERE name = ?", winner)
    desc_dict = desc_list[0]
    desc = desc_dict.get("desc")

    # Switch statement to get club logo image link
    switcher = {
        "Arsenal": "https://i.imgur.com/Dsxy2r3.jpg",
        "Aston Villa": "https://i.imgur.com/fuoYKek.jpg",
        "Brentford": "https://i.imgur.com/ikIDiZ7.jpg",
        "Brighton": "https://i.imgur.com/HBbdU3I.jpg",
        "Chelsea": "https://i.imgur.com/kelI3Eg.jpg",
        "Everton": "https://i.imgur.com/Q4ZR45d.jpg",
        "Leeds": "https://i.imgur.com/d7phkzH.jpg",
        "Leicester": "https://i.imgur.com/yUKc5rv.jpg",
        "Liverpool": "https://i.imgur.com/MyD6JzR.jpg",
        "Manchester City": "https://i.imgur.com/RIf4PXW.jpg",
        "Manchester United": "https://i.imgur.com/7dayYqZ.jpg",
        "Newcastle United": "https://i.imgur.com/CT6vyCm.jpg",
        "Southampton": "https://i.imgur.com/bxgzmUS.jpg",
        "Tottenham Hotspur": "https://i.imgur.com/aevMsh9.jpg",
        "West Ham United": "https://i.imgur.com/TvLllDo.jpg",
        "Wolves": "https://i.imgur.com/YCQZpOK.jpg",

    }
    imagelink = switcher.get(winner)

    return render_template("results.html", winner=winner, desc=desc, imagelink=imagelink)


"""
TO DO :

# Logic
- update descriptions in database
- update results page

# Content
- write team descriptions
- write landing page text

# Styling
- work on style
"""
