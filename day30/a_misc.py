import json

# with open("people.json") as f:  # The mode 'r' is assumed/default
#     file_contents = f.read()
#     all_people = json.loads(file_contents)
#     # all_people = json.load(f)  # Same as above 2 lines.

#     print("DATA:", file_contents, all_people)

#     # print("Age of Meg:", all_people[3]["age"])
#     print("Age of Meg:", all_people[3].get("age"))

with open("people.json") as f:
    all_people = json.load(f)

all_people.append({
    "name": "Roger",
    "age": 23
})

with open("people.json", "w") as f:
    # json_str = json.dumps(all_people)
    # f.write(json_str)
    json.dump(all_people, f, indent=4) # Same as above 2 lines. Indent for "pretty-print"
