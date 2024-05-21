from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def thenameofthisfuctiondoesnotmatter():
    return "<p>Hello world!</p>"

# @app.route("/ping")
# def ping():
# 	return "pong"

@app.route("/ping")
def pong():
  return request.args.get("code") if "code" in request.args else "pong"

@app.get("/nameandcolor")
def name_color():
  in_name = request.args.get('name', 'Adam')
  in_color = request.args.get('color', 'black')
  return f"<h1 style='color: {in_color}'>Hello, {in_name}</h1>"

@app.route("/party")
def partyparty():
  return """
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Party Party!</title>
  <style>
    body {
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
    }
    img {
      height: 400px;
    }
  </style>
</head>

<body>
  <img src="https://gifdb.com/images/high/excited-party-mode-baby-y6ohsg4asvx4171u.webp" alt="Baby NHL Penguins fan is very excited">
</body>
</html>
"""
@app.route("/excited")
def party_baby():
	return "<img src='static/excited-party-mode-baby.webp' alt='Baby NHL Penguins fan is very excited'>"
