# with open("sample.txt", "w") as f:
#     f.write("Hello Priya\n")
#     f.write("This is your first file handling program")
with open("sample.txt", "r") as f:
    data = f.read()
    print(data)