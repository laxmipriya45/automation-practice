# import json

# data = {
#     "name": "Priya",
#     "age": 23,
#     "skills": ["Python", "SQL"]
# }

# with open("data.json", "w") as f:
#     json.dump(data, f)


# import json

# with open("data.json", "r") as f:
#     data = json.load(f)
# print(data)



# import json
# data = {
#     "name":"priya",
#     "age":23,

# }
# with open("example.json","w") as f:
#     json.dump(data,f)


# import json
# data={
#     "name":"resh",
#     "address":"hyderabad",
#     "age":22,
#     "language":"hindi"
# }
# with open("data1.json", "w") as f:
#     json.dump(data, f, indent=4)



import json

data = {
    "name": "resh",
    "address": "hyderabad",
    "age": 22,
    "language": "hindi"
}

with open("data1.json", "w") as f:
    json.dump(data, f, indent=4)

# with open("data1.json", "r") as f:
#     s=json.load(f)
# print(s)


# import json
# d={
#     "name":"kajal",
#     "address":"mumbai"
# }
# with open("d1.json","w") as file:
#     json.dump(d,file, indent=4)


import json
with open("d1.json","r") as f:
    d=json.load(f)
    print(d)

