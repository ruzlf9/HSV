import datetime

import numpy as np
from flask import Flask, jsonify, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'
#app.permanent_session_lifetime = timedelta(seconds=10)

playersu19 = [
  {
    "Vorname": "Ali",
    "Nachname": "Mem",
    "Rating": "A",
    "Geburtsdatum": datetime.datetime(2005, 5, 17).strftime("%x"),
    "Berichte": [{
      "date": datetime.datetime(2022, 5, 17).strftime("%x"),
      "bericht": "Alt Bericht"
                 },
                 {
      "date": datetime.datetime(2023, 5, 17).strftime("%x"),
      "bericht": "Bericht"
    }]
  },
  {
    "Vorname": "Tobias",
    "Nachname": "Muster",
    "Rating": "B",
    "Geburtsdatum": datetime.datetime(2004, 2, 17).strftime("%x"),
    "Berichte": [{
      "date": datetime.datetime(2022, 5, 17).strftime("%x"),
      "bericht": "Alt Bericht"
                 },
                 {
      "date": datetime.datetime(2023, 5, 17).strftime("%x"),
      "bericht": "Bericht"
    }]
  }
]

externalu19 = [
  {
    "Vorname": "Stefan",
    "Nachname": "Neu",
    "Geburtsdatum": datetime.datetime(2005, 2, 11).strftime("%x"),
    "Verein": "DJK TuS Hordel",
    "Berichte": [{
      "date": datetime.datetime(2022, 5, 17).strftime("%x"),
      "bericht": "Alt Bericht"
                 },
                 {
      "date": datetime.datetime(2023, 5, 17).strftime("%x"),
      "bericht": "Bericht"
    }]
  },
  {
    "Vorname": "Paul",
    "Nachname": "Münch",
    "Geburtsdatum": datetime.datetime(2004, 5, 7).strftime("%x"),
    "Verein": "TSC Eintracht Dortmund",
    "Berichte": [{
      "date": datetime.datetime(2022, 5, 17).strftime("%x"),
      "bericht": "Alt Bericht"
                 },
                 {
      "date": datetime.datetime(2023, 5, 17).strftime("%x"),
      "bericht": "Bericht"
    }]
  }
]

playersu17 = [
  {
    "Vorname": "Ali",
    "Nachname": "Mem",
    "Rating": "A",
    "Geburtsdatum": datetime.datetime(2007, 5, 17).strftime("%x"),
    "Berichte": [{
      "date": datetime.datetime(2022, 5, 17).strftime("%x"),
      "bericht": "Alt Bericht"
                 },
                 {
      "date": datetime.datetime(2023, 5, 17).strftime("%x"),
      "bericht": "Bericht"
    }]
  },
  {
    "Vorname": "Tobias",
    "Nachname": "Muster",
    "Rating": "B",
    "Geburtsdatum": datetime.datetime(2007, 2, 17).strftime("%x"),
    "Berichte": [{
      "date": datetime.datetime(2022, 5, 17).strftime("%x"),
      "bericht": "Alt Bericht"
                 },
                 {
      "date": datetime.datetime(2023, 5, 17).strftime("%x"),
      "bericht": "Bericht"
    }]
  }
]

externalu17 = [
  {
    "Vorname": "Stefan",
    "Nachname": "Neu",
    "Geburtsdatum": datetime.datetime(2007, 2, 11).strftime("%x"),
    "Verein": "TSC Eintracht Dortmund",
    "Berichte": [{
      "date": datetime.datetime(2022, 5, 17).strftime("%x"),
      "bericht": "Alt Bericht"
                 },
                 {
      "date": datetime.datetime(2023, 5, 17).strftime("%x"),
      "bericht": "Bericht"
    }]
  },
  {
    "Vorname": "Paul",
    "Nachname": "Münch",
    "Geburtsdatum": datetime.datetime(2007, 5, 7).strftime("%x"),
    "Verein": "BVB",
    "Berichte": [{
      "date": datetime.datetime(2022, 5, 17).strftime("%x"),
      "bericht": "Alt Bericht"
                 },
                 {
      "date": datetime.datetime(2023, 5, 17).strftime("%x"),
      "bericht": "Bericht"
    }]
  }
]

playersu16 = [
  {
    "Vorname": "Ali",
    "Nachname": "Mem",
    "Rating": "A",
    "Geburtsdatum": datetime.datetime(2008, 5, 17).strftime("%x"),
    "Berichte": [{
      "date": datetime.datetime(2022, 5, 17).strftime("%x"),
      "bericht": "Alt Bericht"
                 },
                 {
      "date": datetime.datetime(2023, 5, 17).strftime("%x"),
      "bericht": "Bericht"
    }]
  },
  {
    "Vorname": "Tobias",
    "Nachname": "Muster",
    "Rating": "C",
    "Geburtsdatum": datetime.datetime(2008, 2, 17).strftime("%x"),
    "Berichte": [{
      "date": datetime.datetime(2022, 5, 17).strftime("%x"),
      "bericht": "Alt Bericht"
                 },
                 {
      "date": datetime.datetime(2023, 5, 17).strftime("%x"),
      "bericht": "Bericht"
    }]
  }
]

externalu16 = [
  {
    "Vorname": "Stefan",
    "Nachname": "Neu",
    "Geburtsdatum": datetime.datetime(2008, 2, 11).strftime("%x"),
    "Verein": "FC Brünninghausen",
    "Berichte": [{
      "date": datetime.datetime(2022, 5, 17).strftime("%x"),
      "bericht": "Alt Bericht"
                 },
                 {
      "date": datetime.datetime(2023, 5, 17).strftime("%x"),
      "bericht": "Bericht"
    }]
  },
  {
    "Vorname": "Paul",
    "Nachname": "Münch",
    "Geburtsdatum": datetime.datetime(2008, 5, 7).strftime("%x"),
    "Verein": "Hörder SC",
    "Berichte": [{
      "date": datetime.datetime(2022, 5, 17).strftime("%x"),
      "bericht": "Alt Bericht"
                 },
                 {
      "date": datetime.datetime(2023, 5, 17).strftime("%x"),
      "bericht": "Bericht"
    }]
  }
]

TEAMS = [
  {
    "id": "U19",
    "name": "U19",
    "coaches" : ["Marvin","Justus"],
    "players": playersu19,
    "formation": {'save_formation': 'save', 'LS1': 'Ali_Mem', 'ST1': '', 'RS1': '',
                  'LS2': '', 'ST2': '', 'RS2': '', 'LS3': '', 'ST3': 'Ali_Mem',
                  'RS3': '', 'ZML1': '', 'ZMR1': '', 'ZML2': '', 'ZMR2': '', 
                  'ZML3': '', 'ZMR3': '', 'LV1': '', 'LIV1': '', 'ZIV1': '',
                  'RIV1': '', 'RV1': 'Tobias_Muster', 'LV2': '', 'LIV2': '',
                  'ZIV2': '', 'RIV2': '', 'RV2': '', 'LV3': '', 'LIV3': '',
                  'ZIV3': '', 'RIV3': '', 'RV3': '', 'TW1': '', 'TW2': '',
                  'TW3': ''},
    "external":externalu19
  },
  {
    "id": "U17",
    "name": "U17",
    "coaches" : ["Holger","Rudi"],
    "players": playersu17,
    "formation": {'save_formation': 'save', 'LS1': '', 'ST1': '', 'RS1': '',
      'LS2': '', 'ST2': '', 'RS2': '', 'LS3': '', 'ST3': 'Ali_Mem',
      'RS3': '', 'ZML1': '', 'ZMR1': '', 'ZML2': '', 'ZMR2': '', 
      'ZML3': '', 'ZMR3': '', 'LV1': '', 'LIV1': '', 'ZIV1': '',
      'RIV1': '', 'RV1': 'Tobias_Muster', 'LV2': '', 'LIV2': '',
      'ZIV2': '', 'RIV2': '', 'RV2': '', 'LV3': '', 'LIV3': '',
      'ZIV3': '', 'RIV3': '', 'RV3': '', 'TW1': '', 'TW2': '',
      'TW3': ''},
    "external":externalu17
  },
  {
    "id": "U16",
    "name": "U16",
    "coaches" : ["Lukas","Niklas"],
    "players": playersu16,
    "formation": {'save_formation': 'save', 'LS1': '', 'ST1': '', 'RS1': '',
      'LS2': '', 'ST2': '', 'RS2': '', 'LS3': '', 'ST3': 'Ali_Mem',
      'RS3': '', 'ZML1': '', 'ZMR1': '', 'ZML2': '', 'ZMR2': '', 
      'ZML3': '', 'ZMR3': '', 'LV1': '', 'LIV1': '', 'ZIV1': '',
      'RIV1': '', 'RV1': 'Tobias_Muster', 'LV2': '', 'LIV2': '',
      'ZIV2': '', 'RIV2': '', 'RV2': '', 'LV3': '', 'LIV3': '',
      'ZIV3': '', 'RIV3': '', 'RV3': '', 'TW1': '', 'TW2': '',
      'TW3': ''},
    "external": externalu16
  },
]
ids = {"U19":0, "U17":1, "U16":2}

users = [
  {
  "email": "rudi.zulauf@hombruchersv.de",
  "pw": "rudi",
  "rights": ["U19","U17","U16"]
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

@app.route("/")
def start():
  return render_template("home/home_lock.html", teams=TEAMS)

@app.route("/home")
def home():
  if "user" in session:
    return render_template("home/home.html", teams=TEAMS, 
                           user=session["user"], rights=session["rights"])
  else:
    return render_template('home/home_lock.html', error='Zugangsdaten falsch')
    

@app.route('/login', methods=['POST'])
def login():
  email = request.form.get('email')
  password = request.form.get('password')
  
  for user in users:
    if user["email"] == email and user["pw"] == password:
      session["user"] = email
      session["rights"] = user["rights"]
      return redirect(url_for('home'))
      
  return render_template('home/home_lock.html', error='Zugangsdaten falsch')

@app.route("/logout")
def logout():
  session.pop("user", None)
  session.pop("rights", None)
  return render_template("home/home_lock.html", teams=TEAMS)


@app.route("/<team_id>", methods=['GET', 'POST'])
def team(team_id):
  if "user" in session and team_id in session["rights"]:
    if request.method == 'POST':
      if request.form.get('save_formation') == 'save':
        team = TEAMS[ids[team_id]]
        team["formation"] = request.form.to_dict()
      else:
        pass
    return render_template("team/team.html", team=TEAMS[ids[team_id]], user=session["user"], 
                           teams=TEAMS, rights=session["rights"])
  else:
    return render_template('home/home_lock.html', error='Zugangsdaten falsch')

@app.route("/<team_id>/player/<player_id>", methods=['GET', 'POST'])
def player(team_id, player_id):
  return player_helper(team_id, player_id, external=False)


@app.route("/<team_id>/external/<player_id>", methods=['GET', 'POST'])
def external(team_id, player_id):
  return player_helper(team_id, player_id, external=True)


def player_helper(team_id, player_id, external) -> str:
  type = "external" if external else "players"
  if "user" in session and team_id in session["rights"]:
    team_infos = TEAMS[ids[team_id]]
    ind = np.where((np.array([d['Vorname'] for d in team_infos[type]]) == 
                    player_id.split("_")[0]) & 
                   (np.array([d['Nachname'] for d in team_infos[type]]) == 
                    player_id.split("_")[1]))[0][0]
    player_infos = team_infos[type][ind]

    if request.method == 'POST':
        if request.form.get('save_report') == 'save':
          player_infos["Berichte"].append({"date":
                                           datetime.datetime.today().strftime("%x"),
                                           "bericht":
                                           request.form.get('new_report_text')})
        else:
            pass # unknown
    elif request.method == 'GET':
      return render_template("player/player.html", team=team_infos, 
       player = player_infos, user=session["user"], 
       teams=TEAMS, external=external, rights=session["rights"])

    return render_template("player/player.html", team=team_infos, 
                           player = player_infos, user=session["user"], 
                           teams=TEAMS, external=external, rights=session["rights"])
  else:
    return render_template('home/home_lock.html', error='Zugangsdaten falsch')


@app.route("/api/teams")
def team_jobs():
  if "user" in session:
    return jsonify(TEAMS)
  else:
    return render_template('home/home_lock.html', error='Zugangsdaten falsch')


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)