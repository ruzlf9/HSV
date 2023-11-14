from flask import Flask, render_template

app = Flask(__name__)

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
def hello_world():
  return render_template("home.html", teams=TEAMS)

if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)