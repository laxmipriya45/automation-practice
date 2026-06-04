s=open("demo.txt","r")
print(s.read()) #read
s.close()

s=open("demo1.txt","w")
s.write("priyaa \n") #write
s.write("kommula \n")
s.write("ok ok")
s.close() 

# with open("demo.txt","a", newline="") as f:
# s.writer("hi hloo byee bye") #append

# Open a file in binary write mode
# with open('test.bin', 'wb') as f:
#    # Binary data
#    data = b"Hello World"  
#    f.write(data)



# # Open the file in read mode
# file = open('example.txt', 'r')
# # Read the first line of the file
# line = file.readline()
# # Pint the line
# print(line)
# # Close the file
# file.close()



s=open("ex1.txt", "a")
s.write("ok ok")


s=open("ex1.txt","r")
print(s.read())
# s.close()

# with open("student.txt", "x") as file:  
#     file.write("Name: Priya")

# with open("image.png", "rb") as file:
#     data = file.read()

with open("image.png", "rb") as file:
    data = file.read()
print(type(data))
print(len(data))


with open("image.png", "wb") as file:
    file.write(data)
    

# with open("ex1.txt", "r+") as file:   #read and write both allowed
#     print(file.read())
#     file.write("New Data")