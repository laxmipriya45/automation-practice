# #read
# file = open("example.txt", "r")
# a=file.read();
# print(a)


# # file = open("example.txt", "r")
# # content = file.read()
# # print(content)
# # file.close()

# #write mode
# file=open("example.txt","w")
# file.write("welcome")

# #append
# file=open("example.txt","a")
# file.write(" to python tutorial")



# import csv

# with open("data1.csv", "r") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)


# import csv


# with open("data1.csv", "w", newline="") as f:
#     writer = csv.writer(f)
#     #writer.writerow(["Name", "Age"])
#     writer.writerow(["kommula",24])
#     writer.writerow(["Priya", 22])


# import csv
# with open("data1.csv", "r", newline="") as f:
#     r = csv.writer(f)
# for x in r:
#     print(x)



# x = input("Enter number: ")

# print(x)


# import csv

# with open("students.csv", "w", newline="") as file:

#     writer = csv.writer(file)

#     writer.writerow(["Name", "Age", "City"])
#     writer.writerow(["Priya", 23, "Hyderabad"])
#     writer.writerow(["Rahul", 25, "Delhi"])



# import csv
# with open("students.csv", "r") as file:
#     reader = csv.reader(file)
#     # print(reader)
#     for row in reader:
#         print(row)


# import csv
# with open("students.csv", "r") as file:
#     reader = csv.reader(file)
#     print(list(reader))



import csv
with open("ex11.csv","w", newline="") as f:
    d=csv.writer(f)
    d.writerow(["priya",22])
    d.writerow(["resh",23])


import csv
with open("ex11.csv", "r") as file:
    d=csv.reader(file)
    for x in d:
        print(x)

    