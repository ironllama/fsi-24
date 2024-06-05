from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route("/someapiGet")
def someapiGet():
    return "GOT HERE. You seemed to like " + request.args.get("fav", "nothing") + "!"

@app.route("/someapiPath/<fav>")
def someapiPath(fav):
    return "GOT HERE. You seemed to like " + fav + "!"

@app.route("/someapiPost", methods=['POST'])
def someapiPost():
    # return "GOT HERE. You seemed to like " + str(request.data) + "!"
    return "GOT HERE. You seemed to like " + request.data.decode() + "!"

@app.route("/someapiPostUrl", methods=['POST'])
def someapiPostUrl():
    return "GOT HERE. You seemed to like " + request.form.get("fav", "nothing") + "!"

@app.route("/someapiPostJson", methods=['POST'])
def someapiPostJson():
    return "GOT HERE. You seemed to like " + request.json.get("fav", "nothing") + "!"

@app.get("/getDate")
def getDate():
    orig_date = datetime.fromisoformat("2024-06-03 15:24:11")
    today = datetime.now()
    diff = today - orig_date

    diff_days = diff.days
    diff_hours = diff.seconds // 60 // 60
    diff_minutes = (diff.seconds // 60) - (diff_hours * 60)
    return "today: " + str(today) + " orig: " + str(orig_date) + " delta: " + str(diff_days) + "days " + str(diff_hours) + "hours " + str(diff_minutes) + "min "

# If you want to run the Flask server with standard "python" executable
if __name__ == "__main__":
    app.run(debug=True)
