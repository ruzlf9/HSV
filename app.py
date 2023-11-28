from flask import Flask, render_template, jsonify, request, redirect, url_for, session
from datetime import timedelta


app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.permanent_session_lifetime = timedelta(seconds=10)

TEAMS = [
  {
    "id": "U19",
    "name": "U19",
    "coaches" : ["Marvin","Justus"],
    "players": ["A","B","C"]
  },

  {
    "id": "U17",
    "name": "U17",
    "coaches" : ["Holger","Rudi"],
    "players": ["D","E","F"]
  },

  {
    "id": "U16",
    "name": "U16",
    "coaches" : ["Lukas","Niklas"],
    "players": ["G","H","I"]
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
  print(email)
  print(password)
  
  if authenticate_user(email, password):
    session["user"] = email
    return redirect(url_for('home'))
  else:
    return render_template('home_lock.html', error='Zugangsdaten falsch')

def authenticate_user(email, password):
  return email == 'Test@Test.com' and password == 'password'


@app.route("/api/teams")
def team_jobs():
  return jsonify(TEAMS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)