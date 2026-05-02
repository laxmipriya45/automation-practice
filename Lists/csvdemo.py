import csv

# with open("data.csv", "w", newline="") as f:
#     wx = csv.writer(f)
#     wx.writerow(["Priya", 23])
#     wx.writerow(["srvs",42])

with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
