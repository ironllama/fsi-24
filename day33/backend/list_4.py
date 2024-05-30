# Add in storing data in external files, to keep the same data
# between server restarts.
from flask import Flask, request

app = Flask(__name__)

# To deal with CORS, since our frontend is running on a different
# 'domain'. The browser considers even a change in port numbers as
# separate domains. (eg. Python running on localhost:5000 and our
# ad-hoc web server running on localhost:8000.)
@app.after_request
def apply_caching(response):
    response.headers.set('Access-Control-Allow-Origin', '*')
    response.headers.set('Access-Control-Allow-Methods', 'GET, POST')
    return response

@app.get("/getItems")
def getItems():
    all_items = []
    with open("all_items.db", "r", encoding="utf-8") as f:
        all_items = f.readlines()

    return ",".join(all_items)

@app.post("/newItem")
def newItem():
    item = request.data.decode('utf-8')
    if item:
        with open("all_items.db", "a", encoding="utf-8") as f:
            f.write(item + "\n")
    return "OK"
