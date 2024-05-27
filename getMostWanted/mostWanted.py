"""
    Using the 'allMostWanted.json' file of FBI's most wanted, create an API server that will provide the following endpoints:

    /highbounty
        Find the 20 highest bounties from all the records and return for each record at least the bounty amount, the name of the person and an id.
    
    /details/<person_id>
        Provide a webpage of the details and picture(s) of the person for the id provided in a user-friendly way.
"""
from flask import Flask
import json
import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

app = Flask(__name__)

def getRewardAmount(text):
    if not text: return 0

    start = text.find("$")
    if start != -1:
        end = text.find(" ", start)
        reward_str = text[start + 1: end].replace(",", "")
        return int(float(reward_str))
    else:
        return 0

with open("allMostWanted.json") as f:
    all_records = json.load(f)
    for record in all_records:
        record["bounty"] = getRewardAmount(record["reward_text"])
    all_records.sort(reverse=True, key=lambda r: r["bounty"])

# with open("sortedBounty.json", "w") as f:
#     json.dump(all_records, f)

@app.get("/highbounty")
def highbounty():
    return [{
        "name": record["title"].title(),
        "bounty": record["bounty"],
        "id": record["uid"],
        "subjects": record["subjects"],
        "reward": record["reward_text"]
        }
        for record in all_records[:20]
    ]

@app.get("/details/<person_id>")
def details(person_id):
    for person in all_records:
        if person["uid"] == person_id:
            str_return = f"""
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{person["title"].title()}</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Holtwood+One+SC&display=swap');

        body {{
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background-color: bisque;
            font-weight: bold;
            max-width: 60rem;
            margin: 0 auto;
        }}

        h1,
        h2,
        h3,
        h4 {{
            font-family: "Holtwood One SC", serif;
            margin: 0;
        }}

        img {{
            width: 12rem;
            height: 12rem;
            background-color: grey;
        }}

        p {{
            margin: 0;
        }}
    </style>
</head>

<body>
    <h1 style="font-size:5rem;">WANTED</h1>
    <div style="display:flex; gap:2rem;">
    """
            for img in person["images"]:
                str_return += f"<img src='{img['large']}'>"

            str_return += f"""
    </div>
    <h3 style="font-size:2rem;">{person["title"].title()}</h3>
    <p>
            """
            
            reward_start = person["reward_text"].find("$") if person["reward_text"] else -1
            if reward_start != -1:
                reward_end = person["reward_text"].find(" ", reward_start)
                str_return += person["reward_text"][:reward_start]
                str_return += f"<div style='font-family: Holtwood One SC, serif; font-size:5rem;'>{locale.currency(person['bounty'], grouping=True)}</div>"
                str_return += person["reward_text"][reward_end:]

            str_return += f"""
    </p>
    <h4 style="font-size:1.5rem;">{person["warning_message"]}</h2>
        <p>
            {person["description"]}
        </p>
        <p style="margin-top: 1rem;">
            More information: <a href="{person["url"]}">{person["url"]}</a>
        </p>
</body>

</html>
            """
            return str_return
        
    return f"User with id {person_id} not found."
