from flask import Flask, request

app = Flask(__name__)

@app.post("/stuff")
def stuff():
    one_key = request.json.get("one", "")
    two_key = request.json.get("two", "")

    print("ONTWO:", one_key, two_key)
    return "DONE"
