import datetime

import numpy as np
from flask import Flask, jsonify, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'
#app.permanent_session_lifetime = timedelta(seconds=10)

playersu19 = [
  {
    "Vorname": "Test",
    "Nachname": "Spieler",
    "Geburtsdatum": "11.04.2006",
    "Rating": "A",
    "Berichte": [{
      "date": "11.04.2006",
      "bericht": "Alt Bericht"
                 },
                 {
      "date": "11.04.2006",
      "bericht": "Bericht"
    }]
  },
  {
    "Vorname": "Spieler",
    "Nachname": "Zwei",
    "Geburtsdatum": "11.04.2006",
    "Rating": "B",
    "Berichte": [{
      "date": "11.04.2006",
      "bericht": "Alt Bericht"
                 },
                 {
      "date": "11.04.2006",
      "bericht": "Bericht"
    }]
  }
]

externalu19 = [
  {
    "Vorname": "Externer",
    "Nachname": "Spieler",
    "Verein": "DJK TuS Hordel",
    "Geburtsdatum": "11.04.2006",
    "Rating": "A",
    "Berichte": [{
      "date": "11.04.2006",
      "bericht": "Alt Bericht"
                 },
                 {
      "date": "11.04.2006",
      "bericht": "Bericht"
    }]
  },
  {
    "Vorname": "Anderer",
    "Nachname": "Externer",
    "Verein": "TSC Eintracht",
    "Geburtsdatum": "11.04.2006",
    "Rating": "A",
    "Berichte": [{
      "date": "11.04.2006",
      "bericht": "Alt Bericht"
                 },
                 {
      "date": "11.04.2006",
      "bericht": "Bericht"
    }]
  }
]

playersu17 = [
  {
    "Vorname": "Marlon",
    "Nachname": "Randelhoff",
    "Position": "TW",
    "Geburtsdatum": "01.01.2007",
    "Rating": "C",
    "Berichte": [{
      "date": "11.04.2022",
      "bericht": "Alt Bericht"
                 },
                 {
      "date": "11.04.2023",
      "bericht": "Bericht"
    }]
  },
  {
    "Vorname": "Joshua",
    "Nachname": "Sartorius",
    "Position": "TW",
    "Geburtsdatum": "02.07.2007",
    "Rating": "B",
    "Berichte": [{
      "date": "11.04.2022",
      "bericht": "Alt Bericht"
                 },
                 {
      "date": "11.04.2023",
      "bericht": "Bericht"
    }]
  },
  {
    "Vorname": "Mattis",
    "Nachname": "Linnewerth",
    "Position": "LV",
    "Geburtsdatum": "06.12.2007",
    "Rating": "C",
    "Berichte": [{
      "date": "11.04.2022",
      "bericht": "Alt Bericht"
                 },
                 {
      "date": "11.04.2023",
      "bericht": "Bericht"
    }]
  },
  {
    "Vorname": "Julian",
    "Nachname": "Schneider",
    "Position": "LV",
    "Geburtsdatum": "11.03.2007",
    "Rating": "B",
    "Berichte": [{
      "date": "11.04.2022",
      "bericht": "Alt Bericht"
                 },
                 {
      "date": "11.04.2023",
      "bericht": "Bericht"
    }]
  },
  {
    "Vorname": "Batin",
    "Nachname": "Gökalb",
    "Position": "RV",
    "Geburtsdatum": "17.12.2007",
    "Rating": "B",
    "Berichte": [{
      "date": "11.04.2022",
      "bericht": "Alt Bericht"
                 },
                 {
      "date": "11.04.2023",
      "bericht": "Bericht"
    }]
  },
  {
    "Vorname": "Bakihan",
    "Nachname": "Ayhan",
    "Position": "RV",
    "Geburtsdatum": "01.07.2007",
    "Rating": "C",
    "Berichte": [{
      "date": "11.04.2022",
      "bericht": "Alt Bericht"
                 },
                 {
      "date": "11.04.2023",
      "bericht": "Bericht"
    }]
  },
  {
    "Vorname": "Fabio",
    "Nachname": "Doliwa",
    "Position": "RV",
    "Geburtsdatum": "08.11.2007",
    "Rating": "C",
    "Berichte": [{
      "date": "11.04.2022",
      "bericht": "Alt Bericht"
                 },
                 {
      "date": "11.04.2023",
      "bericht": "Bericht"
    }]
  },
  {
    "Vorname": "Noah",
    "Nachname": "Fell",
    "Position": "IV",
    "Geburtsdatum": "11.11.2007",
    "Rating": "A",
    "Berichte": [{
      "date": "11.04.2022",
      "bericht": "Alt Bericht"
                 },
                 {
      "date": "11.04.2023",
      "bericht": "Bericht"
    }]
  },
  {
    "Vorname": "Luis",
    "Nachname": "Majdanac",
    "Position": "IV",
    "Geburtsdatum": "05.05.2007",
    "Rating": "A",
    "Berichte": [{
      "date": "11.04.2022",
      "bericht": "Alt Bericht"
                 },
                 {
      "date": "11.04.2023",
      "bericht": "Bericht"
    }]
  },
  {
    "Vorname": "Leandro",
    "Nachname": "Tavares",
    "Position": "IV",
    "Geburtsdatum": "06.02.2007",
    "Rating": "B",
    "Berichte": [{
      "date": "11.04.2022",
      "bericht": "Alt Bericht"
                 },
                 {
      "date": "11.04.2023",
      "bericht": "Bericht"
    }]
  },
  {
    "Vorname": "Jan-Luca",
    "Nachname": "Kirchner",
    "Position": "IV",
    "Geburtsdatum": "12.11.2007",
    "Rating": "C",
    "Berichte": [{
      "date": "11.04.2022",
      "bericht": "Alt Bericht"
                 },
                 {
      "date": "11.04.2023",
      "bericht": "Bericht"
    }]
  },
  {
    "Vorname": "Nils",
    "Nachname": "Kleine",
    "Position": "ZM",
    "Geburtsdatum": "05.12.2007",
    "Rating": "B",
    "Berichte": [{
      "date": "11.04.2022",
      "bericht": "Alt Bericht"
                 },
                 {
      "date": "11.04.2023",
      "bericht": "Bericht"
    }]
  },
  {
    "Vorname": "Leon",
    "Nachname": "von Hatzfeld",
    "Position": "ZM",
    "Geburtsdatum": "12.05.2007",
    "Rating": "B",
    "Berichte": [{
      "date": "11.04.2022",
      "bericht": "Alt Bericht"
                 },
                 {
      "date": "11.04.2023",
      "bericht": "Bericht"
    }]
  },
  {
    "Vorname": "Jannik",
    "Nachname": "Leppla",
    "Position": "ZM",
    "Geburtsdatum": "14.01.2007",
    "Rating": "B",
    "Berichte": [{
      "date": "11.04.2022",
      "bericht": "Alt Bericht"
                 },
                 {
      "date": "11.04.2023",
      "bericht": "Bericht"
    }]
  },
  {
    "Vorname": "Kerem",
    "Nachname": "Aksu",
    "Position": "ZM",
    "Geburtsdatum": "19.02.2007",
    "Rating": "C",
    "Berichte": [{
      "date": "11.04.2022",
      "bericht": "Alt Bericht"
                 },
                 {
      "date": "11.04.2023",
      "bericht": "Bericht"
    }]
  },
  {
    "Vorname": "Simon",
    "Nachname": "Strothmüller",
    "Position": "ZM",
    "Geburtsdatum": "22.01.2007",
    "Rating": "B",
    "Berichte": [{
      "date": "11.04.2022",
      "bericht": "Alt Bericht"
                 },
                 {
      "date": "11.04.2023",
      "bericht": "Bericht"
    }]
  },
  {
    "Vorname": "Paul",
    "Nachname": "Stehger",
    "Position": "ZM",
    "Geburtsdatum": "29.04.2007",
    "Rating": "B",
    "Berichte": [{
      "date": "11.04.2022",
      "bericht": "Alt Bericht"
                 },
                 {
      "date": "11.04.2023",
      "bericht": "Bericht"
    }]
  },
  {
    "Vorname": "Japhet",
    "Nachname": "Nsimba",
    "Position": "ST",
    "Geburtsdatum": "14.11.2007",
    "Rating": "C",
    "Berichte": [{
      "date": "11.04.2022",
      "bericht": "Alt Bericht"
                 },
                 {
      "date": "11.04.2023",
      "bericht": "Bericht"
    }]
  },
  {
    "Vorname": "Elton",
    "Nachname": "Kadrija",
    "Position": "ST",
    "Geburtsdatum": "12.12.2007",
    "Rating": "C",
    "Berichte": [{
      "date": "11.04.2022",
      "bericht": "Alt Bericht"
                 },
                 {
      "date": "11.04.2023",
      "bericht": "Bericht"
    }]
  },
  {
    "Vorname": "Jan Luca",
    "Nachname": "Lamay",
    "Position": "ST",
    "Geburtsdatum": "05.09.2007",
    "Rating": "A",
    "Berichte": [{
      "date": "11.04.2022",
      "bericht": "Alt Bericht"
                 },
                 {
      "date": "11.04.2023",
      "bericht": "Bericht"
    }]
  },
  {
    "Vorname": "Kilian",
    "Nachname": "Zierhorst",
    "Position": "ST",
    "Geburtsdatum": "09.09.2007",
    "Rating": "A",
    "Berichte": [{
      "date": "11.04.2022",
      "bericht": "Alt Bericht"
                 },
                 {
      "date": "11.04.2023",
      "bericht": "Bericht"
    }]
  },
  {
    "Vorname": "Joshua",
    "Nachname": "Poll",
    "Position": "ST",
    "Geburtsdatum": "03.03.2007",
    "Rating": "C",
    "Berichte": [{
      "date": "11.04.2022",
      "bericht": "Alt Bericht"
                 },
                 {
      "date": "11.04.2023",
      "bericht": "Bericht"
    }]
  },
  {
    "Vorname": "Dustin",
    "Nachname": "Jurkiewicz",
    "Position": "ST",
    "Geburtsdatum": "09.11.2007",
    "Rating": "B",
    "Berichte": [{
      "date": "11.04.2022",
      "bericht": "Alt Bericht"
                 },
                 {
      "date": "11.04.2023",
      "bericht": "Bericht"
    }]
  },
]

externalu17 = [
  {
    "Vorname": "Externer",
    "Nachname": "Spieler",
    "Verein": "DJK TuS Hordel",
    "Geburtsdatum": "11.04.2006",
    "Rating": "A",
    "Berichte": [{
      "date": "11.04.2006",
      "bericht": "Alt Bericht"
                 },
                 {
      "date": "11.04.2006",
      "bericht": "Bericht"
    }]
  },
  {
    "Vorname": "Anderer",
    "Nachname": "Externer",
    "Verein": "DJK TuS Hordel",
    "Geburtsdatum": "11.04.2006",
    "Rating": "A",
    "Berichte": [{
      "date": "11.04.2006",
      "bericht": "Alt Bericht"
                 },
                 {
      "date": "11.04.2006",
      "bericht": "Bericht"
    }]
  }
]

playersu16 = [
  {
    "Vorname": "Test",
    "Nachname": "Spieler",
    "Geburtsdatum": "11.04.2006",
    "Rating": "A",
    "Berichte": [{
      "date": "11.04.2006",
      "bericht": "Alt Bericht"
                 },
                 {
      "date": "11.04.2005",
      "bericht": "Bericht"
    }]
  },
  {
    "Vorname": "Spieler",
    "Nachname": "Zwei",
    "Geburtsdatum": "11.04.2006",
    "Rating": "C",
    "Berichte": [{
      "date": "11.04.2006",
      "bericht": "Alt Bericht"
                 },
                 {
      "date": "11.04.2006",
      "bericht": "Bericht"
    }]
  }
]

externalu16 = [
  {
    "Vorname": "Externer",
    "Nachname": "Spieler",
    "Verein": "DJK TuS Hordel",
    "Geburtsdatum": "11.04.2006",
    "Rating": "A",
    "Berichte": [{
      "date": "11.04.2006",
      "bericht": "Alt Bericht"
                 },
                 {
      "date": "11.04.2006",
      "bericht": "Bericht"
    }]
  },
  {
    "Vorname": "Anderer",
    "Nachname": "Externer",
    "Verein": "DJK TuS Hordel",
    "Geburtsdatum": "11.04.2006",
    "Rating": "A",
    "Berichte": [{
      "date": "11.04.2006",
      "bericht": "Alt Bericht"
                 },
                 {
      "date": "11.04.2006",
      "bericht": "Bericht"
    }]
  }
]

TEAMS = [
  {
    "id": "U19",
    "name": "U19",
    "players": playersu19,
    "formation": {'save_formation': 'save', 'LS1': 'Test_Spieler', 'ST1': '', 'RS1': '',
                  'LS2': '', 'ST2': '', 'RS2': '', 'LS3': '', 'ST3': 'Spieler_Zwei',
                  'RS3': '', 'ZML1': '', 'ZMR1': '', 'ZML2': '', 'ZMR2': '', 
                  'ZML3': '', 'ZMR3': '', 'LV1': '', 'LIV1': '', 'ZIV1': '',
                  'RIV1': '', 'RV1': '', 'LV2': '', 'LIV2': '',
                  'ZIV2': '', 'RIV2': '', 'RV2': '', 'LV3': '', 'LIV3': '',
                  'ZIV3': '', 'RIV3': '', 'RV3': '', 'TW1': '', 'TW2': '',
                  'TW3': ''},
    "external":externalu19
  },
  {
    "id": "U17",
    "name": "U17",
    "players": playersu17,
    "formation": {'save_formation': 'save', 'LS1': 'Dustin_Jurkiewicz', 'ST1': 'Jan Luca_Lamay', 'RS1': 'Kilian_Zierhorst', 'LS2': 'Japhet_Nsimba', 'ST2': 'Joshua_Poll', 'RS2': 'Elton_Kadrija', 'LS3': '', 'ST3': '', 'RS3': '', 'ZML1': 'Paul_Stehger', 'ZMR1': 'Simon_Strothmüller', 'ZML2': 'Jannik_Leppla', 'ZMR2': 'Leon_von Hatzfeld', 'ZML3': 'Kerem_Aksu', 'ZMR3': 'Nils_Kleine', 'LV1': 'Julian_Schneider', 'LIV1': 'Luis_Majdanac', 'ZIV1': 'Noah_Fell', 'RIV1': 'Leandro_Tavares', 'RV1': 'Batin_Gökalb', 'LV2': 'Mattis_Linnewerth', 'LIV2': 'Jan-Luca_Kirchner', 'ZIV2': '', 'RIV2': '', 'RV2': 'Bakihan_Ayhan', 'LV3': '', 'LIV3': '', 'ZIV3': '', 'RIV3': '', 'RV3': 'Fabio_Doliwa', 'TW1': 'Joshua_Sartorius', 'TW2': 'Marlon_Randelhoff', 'TW3': ''},
    "external":externalu17
  },
  {
    "id": "U16",
    "name": "U16",
    "players": playersu16,
    "formation": {'save_formation': 'save', 'LS1': '', 'ST1': '', 'RS1': '',
      'LS2': '', 'ST2': '', 'RS2': '', 'LS3': '', 'ST3': 'Spieler_Zwei',
      'RS3': '', 'ZML1': '', 'ZMR1': '', 'ZML2': '', 'ZMR2': '', 
      'ZML3': '', 'ZMR3': '', 'LV1': '', 'LIV1': '', 'ZIV1': '',
      'RIV1': '', 'RV1': 'Test_Spieler', 'LV2': '', 'LIV2': '',
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
    "email": "dominik.starke@hombruchersv.de",
    "pw": "HSV",
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
      print("===========================================")
      print(request.form)
      print("===========================================")
      
      # Sort player list
      if request.form.get("sort_players") != None:
        team = TEAMS[ids[team_id]]
        formation = team["formation"]
        type, action = request.form.get("sort_players").split("_")

        type = "players" if type == "own" else "external"

        print(type, action)
        
        players = team[type] 
        names = [p.split("_") for p in formation.values()]
        colors = ["#ffffff" if len(n)==1 else 
                  next((rating_mapping(player["Rating"]) for player in team["players"] if 
                        player["Vorname"] == n[0] 
                        and player["Nachname"] == n[1]), None)
                  for n in names][1:]
        sorted_players = players
        
        if action == "vorn.inc":
          print(players)
          sorted_players = sorted(players, key=lambda x: x['Vorname'].upper())
          print(sorted_players)
        if action == "vorn.dec":
          sorted_players = sorted(players, key=lambda x: x['Vorname'].upper(), reverse=True)
          
        if action == "nachn.inc":
          sorted_players = sorted(players, key=lambda x: x['Nachname'].upper())
        if action == "nachn.dec":
          sorted_players = sorted(players, key=lambda x: x['Nachname'].upper(), reverse=True)
          
        if action == "gebdat.inc":
          sorted_players = sorted(players, key=lambda x: 
                                  (int(x['Geburtsdatum'].split(".")[2]), 
                                  int(x['Geburtsdatum'].split(".")[1]),
                                  int(x['Geburtsdatum'].split(".")[0])))
        if action == "gebdat.dec":
          sorted_players = sorted(players, key=lambda x: 
            (int(x['Geburtsdatum'].split(".")[2]), 
            int(x['Geburtsdatum'].split(".")[1]),
            int(x['Geburtsdatum'].split(".")[0])), reverse=True)
          
        if action == "rating.inc":
          sorted_players = sorted(players, key=lambda x: x['Rating'])
        if action == "rating.dec":
          sorted_players = sorted(players, key=lambda x: x['Rating'], reverse=True)

        if type == "players":
          return render_template("team/team.html", team=TEAMS[ids[team_id]], 
           user=session["user"], 
           teams=TEAMS, rights=session["rights"], 
           colors_formation=colors, players=sorted_players, externals=team["external"])
        else:
          return render_template("team/team.html", team=TEAMS[ids[team_id]], 
             user=session["user"], 
             teams=TEAMS, rights=session["rights"], 
             colors_formation=colors, players=team["players"], externals=sorted_players)

      
      # Delete own Player
      if request.form.get("delete_player") != None:
        team = TEAMS[ids[team_id]]
        player = request.form.get("delete_player")
        vorname = player.split("_")[0]
        nachname = player.split("_")[1]
        team["players"] = [p for p in team["players"] if 
                           p.get('Vorname') != vorname and 
                           p.get("Nachname") != nachname]
        return redirect(location="/"+team_id)

      # Delete external Player
      if request.form.get("delete_external_player") != None:
        team = TEAMS[ids[team_id]]
        player = request.form.get("delete_external_player")
        vorname = player.split("_")[0]
        nachname = player.split("_")[1]
        team["external"] = [p for p in team["external"] if 
                           p.get('Vorname') != vorname and 
                           p.get("Nachname") != nachname]
        return redirect(location="/"+team_id)
        
      # Add own player
      if request.form.get("add_player") == "False":
        team = TEAMS[ids[team_id]]

        gebdatum = request.form.get("gebdatum")

        new_player = {'Vorname': request.form.get("vorname"), 
                      'Nachname': request.form.get("nachname"), 
                      'Geburtsdatum': gebdatum, 
                      'Rating': request.form.get("rating"), 
                      'Berichte': [{'date': str(datetime.datetime.today().day)+
                                     "."+str(datetime.datetime.today().month)+
                                     "."+str(datetime.datetime.today().year), 
                                    'bericht': request.form.get("report")}
                                   ]}
        
        team["players"].append(new_player)

      # Add external player
      if request.form.get("add_player") == "True":
        team = TEAMS[ids[team_id]]
  
        gebdatum = request.form.get("gebdatum")
  
        new_player = {'Vorname': request.form.get("vorname"), 
                      'Nachname': request.form.get("nachname"), 
                      "Verein": request.form.get("verein"),
                      'Geburtsdatum': gebdatum, 
                      'Rating': request.form.get("rating"), 
                      'Berichte': [{'date': str(datetime.datetime.today().day)+
                                     "."+str(datetime.datetime.today().month)+
                                     "."+str(datetime.datetime.today().year), 
                                    'bericht': request.form.get("report")}
                                   ]}
  
        team["external"].append(new_player)

      # Go to page to add new player
      if request.form.get('new_player') == 'own':
        return render_template("team/new_player.html", 
                               team=TEAMS[ids[team_id]], user=session["user"], 
                               teams=TEAMS,
                               rights=session["rights"],external=False)

      # Go to page to add external player
      if request.form.get('new_player') == 'external':
        return render_template("team/new_player.html", team=TEAMS[ids[team_id]], user=session["user"], 
                               teams=TEAMS, rights=session["rights"], external=True)

      # Save current formation
      if request.form.get('save_formation') == 'save':
        team = TEAMS[ids[team_id]]
        print(team["formation"])
        team["formation"] = request.form.to_dict()
        print(team["formation"])
      else:
        pass
    team = TEAMS[ids[team_id]]
    formation = team["formation"]
    players = team["players"]
    names = [p.split("_") for p in formation.values()]
    colors = ["#ffffff" if len(n)==1 else 
              next((rating_mapping(player["Rating"]) for player in players if 
                    player["Vorname"] == n[0] 
                    and player["Nachname"] == n[1]), None)
              for n in names][1:]
    return render_template("team/team.html", team=TEAMS[ids[team_id]], 
                           user=session["user"], 
                           teams=TEAMS, rights=session["rights"], 
                           colors_formation=colors, 
                           players=sorted(players, key=lambda x: x['Nachname'].upper()),
                           externals = sorted(team["external"], key=lambda x: x['Nachname'].upper()))
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
      print("-------------------------")
      print(request.form)
      print("--------------------------")

      # Delete player
      if request.form.get("delete_player") != None:
        team = TEAMS[ids[team_id]]
        player = request.form.get("delete_player")
        vorname = player.split("_")[0]
        nachname = player.split("_")[1]
        team["players"] = [p for p in team["players"] if 
                           p.get('Vorname') != vorname and 
                           p.get("Nachname") != nachname]
        return redirect(location="/"+team_id)


      # Delete external Player
      if request.form.get("delete_external_player") != None:
        team = TEAMS[ids[team_id]]
        player = request.form.get("delete_external_player")
        vorname = player.split("_")[0]
        nachname = player.split("_")[1]
        team["external"] = [p for p in team["external"] if 
                           p.get('Vorname') != vorname and 
                           p.get("Nachname") != nachname]
        return redirect(location="/"+team_id)

      # Save new report
      if request.form.get('save_report') == 'save':
        player_infos["Berichte"].insert(0,
                                        {"date": str(datetime.datetime.today().day)+
                                         "."+str(datetime.datetime.today().month)+
                                         "."+str(datetime.datetime.today().year),
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


@app.route("/<team_id>/player/<player_id>/edit", methods=['GET', 'POST'])
def player_edit(team_id, player_id):
  return edit_player(team_id, player_id, external=False)


@app.route("/<team_id>/external/<player_id>/edit", methods=['GET', 'POST'])
def external_edit(team_id, player_id):
  return edit_player(team_id, player_id, external=True)


def edit_player(team_id, player_id, external):
  type = "external" if external else "players"
  if "user" in session and team_id in session["rights"]:
    team_infos = TEAMS[ids[team_id]]
    ind = np.where((np.array([d['Vorname'] for d in team_infos[type]]) == 
                    player_id.split("_")[0]) & 
                   (np.array([d['Nachname'] for d in team_infos[type]]) == 
                    player_id.split("_")[1]))[0][0]
    player_infos = team_infos[type][ind]

    # save changes
    if request.method == 'POST':
      print("====================================")
      print(request.form)
      print("====================================")
      if request.form.get('save_changes') == 'save':
        player_infos["Vorname"] = request.form.get('vorname')
        player_infos["Nachname"] = request.form.get('nachname')
        player_infos["Geburtsdatum"] = request.form.get('gebdatum')
        player_infos["Rating"] = request.form.get('rating').strip()
        if type == "external":
          player_infos["Verein"] = request.form.get('verein')
        return redirect(location="/"+team_id)
      else:
          pass # unknown

    elif request.method == 'GET':
      return render_template("player/player_edit.html", team=team_infos, 
       player = player_infos, user=session["user"], 
       teams=TEAMS, external=external, rights=session["rights"])

    return render_template("player/player_edit.html", team=team_infos, 
                           player = player_infos, user=session["user"], 
                           teams=TEAMS, 
                           external=external, rights=session["rights"])
  else:
    return render_template('home/home_lock.html', error='Zugangsdaten falsch')


def rating_mapping(rating):
  rating_colors = {
    "A": "#16B13D",
    "B": "#7BB11B",
    "C": "#B19719",
    "D": "#B1671E",
    "E": "#B12B1D"
  }
  return rating_colors.get(rating.strip(), "default_color")
  


@app.route("/api/teams")
def team_jobs():
  if "user" in session:
    return jsonify(TEAMS)
  else:
    return render_template('home/home_lock.html', error='Zugangsdaten falsch')


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)