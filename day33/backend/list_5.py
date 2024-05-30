# Using JSON as the data structure of the messages between frontend
# and backend
from flask import Flask, request
import json

app = Flask(__name__)

# To deal with CORS, since our frontend is running on a different
# 'domain'. The browser considers even a change in port numbers as
# separate domains. (eg. Python running on localhost:5000 and our
# ad-hoc web server running on localhost:8000.)
@app.after_request
def apply_caching(response):
    response.headers.set('Access-Control-Allow-Origin', '*')
    response.headers.set('Access-Control-Allow-Methods', 'GET, POST')

    # For application/json support
    response.headers.set('Access-Control-Allow-Headers', 'Content-Type')

    return response

@app.get("/getItems")
def getItems():
    all_items = []
    with open("all_items.db5", "r", encoding="utf-8") as f:
        all_lines = f.readlines()
        all_items = [json.loads(line) for line in all_lines]

    return all_items

@app.post("/newItem")
def newItem():
    # This avoids having to pull apart the object, just to rebuild it before
    # writing it to the file.
    # json_str = request.data.decode("utf-8")
    # if json_str:
    #     with open("all_items.db5", "a", encoding="utf-8") as f:
    #         f.write(json_str + "\n")

    # Same as above, but processing the json items individually
    amt = request.json.get("amt", 0)
    item = request.json.get("item", "")

    if item:
        item_dict = { "amt": amt, "item": item }  # Rebuild object.
        json_str = json.dumps(item_dict)

        with open("all_items.db5", "a", encoding="utf-8") as f:
            f.write(json_str + "\n")

    return { "message": "OK" }
