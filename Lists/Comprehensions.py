nums = [1, 2, 3, 4, 5]

# list
l = [x*2 for x in nums]

# set
s = {x*2 for x in nums}

# dict
d = {x: x*2 for x in nums}

# tuple
t = tuple(x*2 for x in nums)

print(l)
print(s)
print(d)
print(t)