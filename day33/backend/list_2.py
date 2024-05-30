# Instead of forcing the front-end to redirect back to the form
# after submitting newItems, this one assumes the front end is
# running AJAX (or doesn't make any endpoint consumer assumptions)
# and just returns an 'OK'.
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
    item = request.data
    if item:
        all_items.append(item.decode('utf-8'))
    print("ALL_ITEMS:", all_items)
    return "OK"
