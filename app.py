from flask import Flask, render_template, jsonify, request, redirect, url_for, session
from datetime import timedelta
import datetime
import numpy as np
from flask.typing import TemplateTestCallable


app = Flask(__name__)
app.secret_key = 'your_secret_key'
#app.permanent_session_lifetime = timedelta(seconds=10)

TEAMS = [
  {
    "id": "U19",
    "name": "U19",
    "coaches" : ["Marvin","Justus"],
    "players": [
      {
        "Vorname": "Justin",
        "Nachname": "Test",
        "Geburtsdatum": datetime.datetime(2020, 5, 17).strftime("%x")
      },
      {
        "Vorname": "Justin",
        "Nachname": "Test",
        "Geburtsdatum": datetime.datetime(2020, 5, 17).strftime("%x")
      }
    ]
  },

  {
    "id": "U17",
    "name": "U17",
    "coaches" : ["Holger","Rudi"],
    "players": [
      {
        "Vorname": "Justin",
        "Nachname": "Test",
        "Geburtsdatum": datetime.datetime(2020, 5, 17).strftime("%x")
      },
      {
        "Vorname": "Justin",
        "Nachname": "Test",
        "Geburtsdatum": datetime.datetime(2020, 5, 17).strftime("%x")
      }
    ]
  },

  {
    "id": "U16",
    "name": "U16",
    "coaches" : ["Lukas","Niklas"],
    "players": [
      {
        "Vorname": "Justin",
        "Nachname": "Test",
        "Geburtsdatum": datetime.datetime(2020, 5, 17).strftime("%x")
      },
      {
        "Vorname": "Justin",
        "Nachname": "Test",
        "Geburtsdatum": datetime.datetime(2020, 5, 17).strftime("%x")
      }
    ]
  }
]
ids = {"U19":0, "U17":1, "U16":2}

users = [
  {
  "email": "U19@U19.com",
  "pw": "U19",
  "rights": ["U19","U17"]
},
  {
  "email": "U17@U17.com",
  "pw": "U17",
  "rights": ["U17"]
},
  {
  "email": "U16@U16.com",
  "pw": "U16",
  "rights": ["U16"]
}]

EXTERNAL_PLAYERS = [
  {
    "Vorname": "Test",
    "Nachname": "Nachname",
    "Geburtsdatum": datetime.datetime(2020, 5, 17).strftime("%x")
  },
  {
    "Vorname": "Test2",
    "Nachname": "Nachname2",
    "Geburtsdatum": datetime.datetime(2020, 5, 17).strftime("%x")
  }
]

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
    return render_template("team.html", team=TEAMS[ids[team_id]], user=session["user"], teams=TEAMS)
  else:
    return render_template('home_lock.html', error='Zugangsdaten falsch')

@app.route("/<team_id>/player/<player_id>")
def player(team_id, player_id):
  if "user" in session:
    team_infos = TEAMS[ids[team_id]]
    print("------------------------------")
    print(team_infos)
    ind = np.where((np.array([d['Vorname'] for d in team_infos["players"]]) == player_id.split("_")[0]) & (np.array([d['Nachname'] for d in team_infos["players"]]) == player_id.split("_")[1]))[0][0]
    player_infos = team_infos["players"][ind]
    
    return render_template("player.html", team=team_infos, player = player_infos, user=session["user"], teams=TEAMS)
  else:
    return render_template('home_lock.html', error='Zugangsdaten falsch')


@app.route("/external")
def external():
  if "user" in session:
    return render_template("external.html", user=session["user"], players=EXTERNAL_PLAYERS, teams=TEAMS)
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