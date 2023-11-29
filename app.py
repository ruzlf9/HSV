from flask import Flask, render_template, jsonify, request, redirect, url_for, session
from datetime import timedelta
import datetime


app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.permanent_session_lifetime = timedelta(seconds=10)

TEAMS = [
  {
    "id": "U19",
    "name": "U19",
    "coaches" : ["Marvin","Justus"],
    "players": [
      {
        "name": "Justin_Test",
        "birthdate": datetime.datetime(2020, 5, 17).strftime("%x")
      },
      {
        "name": "Tim_Test",
        "birthdate": datetime.datetime(2020, 8, 12).strftime("%x")
      }
    ]
  },

  {
    "id": "U17",
    "name": "U17",
    "coaches" : ["Holger","Rudi"],
    "players": [
      {
        "name": "Ali_Test",
        "birthdate": datetime.datetime(2021, 2, 2).strftime("%x")
      },
      {
        "name": "Noah_Test",
        "birthdate": datetime.datetime(2021, 4, 19).strftime("%x")
      }
    ]
  },

  {
    "id": "U16",
    "name": "U16",
    "coaches" : ["Lukas","Niklas"],
    "players": [
      {
        "name": "Younes_Test",
        "birthdate": datetime.datetime(2022, 2, 19).strftime("%x")
      },
      {
        "name": "Joshua_Test",
        "birthdate": datetime.datetime(2022, 8, 12).strftime("%x")
      }
    ]
  }
]
ids = {"U19":0, "U17":1, "U16":2}

@app.route("/")
def start():
  return render_template("home_lock.html", teams=TEAMS)

@app.route("/home")
def home():
  if "user" in session:
    return render_template("home.html", teams=TEAMS, user=session["user"])
  else:
    return render_template('home_lock.html', error='Zugangsdaten falsch')
    

@app.route('/login', methods=['POST'])
def login():
  email = request.form.get('email')
  password = request.form.get('password')
  print(email)
  print(password)
  
  if authenticate_user(email, password):
    session["user"] = email
    return redirect(url_for('home'))
  else:
    return render_template('home_lock.html', error='Zugangsdaten falsch')

def authenticate_user(email, password):
  return email == 'Test@Test.com' and password == 'password'


@app.route("/<team_id>")
def team(team_id):
  if "user" in session:
    print(TEAMS[ids[team_id]]["name"])
    return render_template("team.html", team=TEAMS[ids[team_id]], user=session["user"])
  else:
    return render_template('home_lock.html', error='Zugangsdaten falsch')


@app.route("/api/teams")
def team_jobs():
  if "user" in session:
    return jsonify(TEAMS)
  else:
    return render_template('home_lock.html', error='Zugangsdaten falsch')


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)