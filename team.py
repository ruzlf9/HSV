from helping import rating_mapping
from flask import Flask, jsonify, redirect, render_template, request, session, url_for

def transfer_player(req, TEAMS, ids, team_id):
  player, new_team = req.split("&")

  current_team = TEAMS[ids[team_id]]
  new_team = TEAMS[ids[new_team]]

  vorname, nachname = player.split("_")

  player_infos = [p for p in current_team["players"] if 
                  p.get('Vorname') == vorname and 
                  p.get("Nachname") == nachname][0]

  player_infos_new = [p for p in new_team["players"] if 
                      p.get('Vorname') == vorname and 
                      p.get("Nachname") == nachname]

  if len(player_infos_new) == 0:
    new_team["players"].append(player_infos)

  team = TEAMS[ids[team_id]]
  formation = team["formation"]
  players = team["players"]
  names = [p.split("_") for p in formation.values()]
  colors = ["#ffffff" if len(n)==1 else 
            next((rating_mapping(player["Rating"]) for player in players if 
                  player["Vorname"] == n[0] 
                  and player["Nachname"] == n[1]), None)
            for n in names]
  
  return render_template("team/team.html", team=TEAMS[ids[team_id]], 
                         user=session["user"], 
                         teams=TEAMS, rights=session["rights"], 
                         colors_formation=colors, 
                         players=sorted(players, key=lambda x: x['Nachname'].upper()),
                         externals = sorted(team["external"], key=lambda x: 
                                            x['Nachname'].upper()))

def transfer_external_player(req, TEAMS, ids, team_id):
  player, new_team = req.split("&")

  current_team = TEAMS[ids[team_id]]
  new_team = TEAMS[ids[new_team]]

  vorname, nachname = player.split("_")

  player_infos = [p for p in current_team["external"] if 
                  p.get('Vorname') == vorname and 
                  p.get("Nachname") == nachname][0]

  player_infos_new = [p for p in new_team["external"] if 
                      p.get('Vorname') == vorname and 
                      p.get("Nachname") == nachname]

  if len(player_infos_new) == 0:
    new_team["external"].append(player_infos)

  team = TEAMS[ids[team_id]]
  formation = team["formation"]
  players = team["players"]
  names = [p.split("_") for p in formation.values()]
  colors = ["#ffffff" if len(n)==1 else 
            next((rating_mapping(player["Rating"]) for player in players if 
                  player["Vorname"] == n[0] 
                  and player["Nachname"] == n[1]), None)
            for n in names]
  return render_template("team/team.html", team=TEAMS[ids[team_id]], 
                         user=session["user"], 
                         teams=TEAMS, rights=session["rights"], 
                         colors_formation=colors, 
                         players=sorted(players, key=lambda x: x['Nachname'].upper()),
                         externals = sorted(team["external"], key=lambda x: 
                                            x['Nachname'].upper()))

def sort_player_list(req, TEAMS, ids, team_id):
  team = TEAMS[ids[team_id]]
  formation = team["formation"]
  type, action = req.split("_")

  type = "players" if type == "own" else "external"

  print(type, action)

  players = team[type] 
  names = [p.split("_") for p in formation.values()]
  colors = ["#ffffff" if len(n)==1 else 
            next((rating_mapping(player["Rating"]) for player in team["players"] if 
                  player["Vorname"] == n[0] 
                  and player["Nachname"] == n[1]), None)
            for n in names]
  sorted_players = players

  if action == "vorn.inc":
    sorted_players = sorted(players, key=lambda x: x['Vorname'].upper())
  if action == "vorn.dec":
    sorted_players = sorted(players, key=lambda x: x['Vorname'].upper(), reverse=True)

  if action == "nachn.inc":
    sorted_players = sorted(players, key=lambda x: x['Nachname'].upper())
  if action == "nachn.dec":
    sorted_players = sorted(players, key=lambda x: x['Nachname'].upper(), reverse=True)

  if action == "verein.inc":
    sorted_players = sorted(players, key=lambda x: x['Verein'].upper())
  if action == "verein.dec":
    sorted_players = sorted(players, key=lambda x: x['Verein'].upper(), reverse=True)

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

  return sorted_players, type, colors, team
