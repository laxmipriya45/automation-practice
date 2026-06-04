person = {
    "name": "Priya",
    "age": 22,
    "city": "Hyderabad"
}
person["age"]=23;
print(person["age"])
#print(person["name"]) #access elements
print(person)
#person["age"] = 23 #modify
#print(person["age"])

#Get key + value pairs
human={
    "name":"priya",
    "age":23 ,
    "address":"hyd"
}
for key, value in human.items():
    print(key, value)



