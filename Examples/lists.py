##fruits = ["apple", "banana", "mango"]
##print(fruits[-1]);
##
###Changing Values
##fruits[2]="dragon"
##print(fruits[2])
##
##fruits.append("grapes")
##print(fruits)
##
##fruits.insert(1, "kiwi")
##print(fruits)
##
##fruits.remove("apple")
##print(fruits)
##print(len(fruits))

##fruits.pop(1)

#list slicing
##numbers = [1, 2, 3, 4, 5]
##
##print(numbers[1:4])  # [2, 3, 4]


#List methods
##nums = [3, 1, 4, 2]
##nums.sort()      # [1, 2, 3, 4]
##nums.reverse()   # [4, 3, 2, 1]
####nums.count(2)    # count occurrences
####nums.index(3)    # find position
##
##print(nums)


##fruits = ['apple', 'banana', 'cherry', 'orange']
##x = fruits.copy()
##print(x)


# fruits = ["apple", "banana", "cherry"]
# x = fruits.count("cherry")
# print(x)


# Access elements (index)
# fruits = ["apple", "banana", "cherry"]
# print(fruits[0])   # apple
# print(fruits[1])   # banana


# Modify list (changeable)
fruits = ["apple", "banana", "cherry"]
# fruits[1] = "orange"
fruits.append("mango")  
print(fruits)
# fruits.append("mango")   # add at end (add elements)


x=["priya","selena","justin"]  #remove elements
x.remove("justin")
print(x)

#loop through list
for fruit in fruits:
    print(fruit)

print(len(fruits)) #length of the fruits

# allow duplicates also
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)


# mylist = ["apple", "banana", "cherry"]
# print(type(mylist))


#dynamically
lists = input("Enter values: ").split()
print(lists)
