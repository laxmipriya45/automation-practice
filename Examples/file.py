# s=open("p.txt","w")  #write
# s.write("hello")

# s=open("p.txt","r")     #read
# print(s.read())


# s=open("p.txt","a")
# s.write("ok ok ")

# import csv
# with open("p.csv","w", newline="") as f:
#     s=csv.writer(f)
#     s.writerow(["Names","address"])
#     s.writerow(["kajal","bombay"])
#     s.writerow(["Tammanah","Gujarat"])

import csv
with open("p.csv","r") as f:
    s=csv.reader(f)
    print(list(s))

import csv
with open("p.csv","r") as f:
    s=csv.reader(f)
    for x in s:
        print(x)

import json
with open("d1.json","r") as f:
    s=json.load(f)
    print(s)

        
# import json
# data={
#     "name":"priya",
#     "age":"hyd"
# }
# with open("d1.json", "w") as f:
#     json.dump(data,f, indent=4)


# import json
# with open("d1.json","r") as f:
#     s=json.load(f)
#     print(s)