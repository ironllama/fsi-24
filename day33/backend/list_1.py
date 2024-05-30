from flask import Flask, request

app = Flask(__name__)

all_items = []

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
    return ",".join(all_items)

@app.post("/newItem")
def newItem():
    item = request.form.get("item")
    all_items.append(item)
    return "<meta http-equiv='refresh' content='0; url=http://localhost:8000/list_1.html' />"
