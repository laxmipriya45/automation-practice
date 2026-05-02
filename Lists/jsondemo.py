# import json

# data = {
#     "name": "Priya",
#     "age": 23,
#     "skills": ["Python", "SQL"]
# }

# with open("data.json", "w") as f:
#     json.dump(data, f)


import json

with open("data.json", "r") as f:
    data = json.load(f)

print(data)