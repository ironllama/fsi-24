from flask import Flask, render_template, request

app = Flask(__name__)

@app.get("/ping")
def ping():
  return "pong"

@app.get("/")
def index():
  name = request.args.get('firstname', 'Alvin')
  return render_template("personal_greeting.html", user=name)

@app.get("/home")
def home():
  return render_template("home.html")
