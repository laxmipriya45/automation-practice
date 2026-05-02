# square of numbers
squares = [x*x for x in range(5)]
print(squares)

# even numbers
even = [x for x in range(10) if x % 2 == 0]
print(even)


# set (unique squares)
s = {x*x for x in [1, 2, 2, 3]}
print(s)
# remove duplicates
nums = {x for x in [1,1,2,3,3,4]}
print(nums)


# dict (key-value pairs)
d = {x: x*x for x in range(5)}
print(d)
# only even keys
d2 = {x: x*x for x in range(10) if x % 2 == 0}
print(d2)


# Tuple (Generator Expression)
# generator (not actual tuple)
t = (x*x for x in range(5))
print(t)
# convert to tuple
t2 = tuple(x*x for x in range(5))
print(t2)

