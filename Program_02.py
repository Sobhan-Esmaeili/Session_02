"""
Dr. Sobhan Esmaeili | Postdoctoral Researcher in Computer and Telecommunication Networks
Statistical Pattern Recognition | Session 02
"""
# Else Statements
# using an else statement
# name = "Sobhan"
# if name == "Reza":
#     print("Hello Reza!")
# else:
#     print("Hello {0}!".format(name))


# Writing a Full Conditional Statement with if, elif, else
# name = "Sobhan"
# if name[0] == "S":
#     print("Name Starts with an S")
# elif name[0] == "E":
#     print("Name Starts with a E")
# elif name[0] == "M":
#     print("Name Starts with a M")
# else:
#     print("Name starts with a {0}".format(name[0]))  # Covers all Other Possibilities


# Lists
# Declaring a List of Numbers
# nums = [5, 10, 15.2, 20]
# print(nums)

# Accessing Elements Within a List
# nums = [5, 10, 15.2, 20]
# print(nums)
# print(nums[1])  # Will Output the Value at Index 1 = 10
# num = nums[2]  # Saves Index Value 2 Into num
# print(num)  # prints value assigned to num


# Declaring a List of Mixed Data Types
# num = 4.3
# data = [num, "word", True]  # the Power of Data Collection
# print(data)


# Understanding Lists Within Lists
# data = ["Reza", 35, ["Sobhan", 36], True]  # lists can hold any type
# print(data)
# print(data[2])


# Using Double Bracket Notation to Access Lists Within Lists
# data = ["Reza", 35, ["Sobhan", 36], True]
# print(data[2][0])  # Will Output Sobhan
# inner_list = data[2]  # Inner List Will Equal ["Sobhan", 36]
# print( inner_list[1])  # Will Output 36


# Changing Values in a List Through Index
# data = [5, 10, 15, 20]
# print(data)
# data[0] = 100  # change the value at index 0 - (5 to 100)
# print(data)


# Variable Storage
# a = [5, 10]
# print(id(a)) # Large Number Represents Location in Memory


# Understanding How Lists are Stored
# a = [5, 10]
# b = a
# print("a: {0}\t b: {1}".format(a, b))
# print("Location a[0]: {0}\t Location b[0]: {1}".format(id(a[0]), id(b[0])))
# a[0] = 20  # Re-Declaring the Value of a[0] Also Changes b[0]
# print("a: {0}\t b: {1}".format(a, b))


# Copying a List
# using [:] to copy a list
# data = [5, 10, 15, 20]
# data_copy = data[:]  # a single colon copies the list
# data[0] = 50
# print("data: {0}\t data_copy: {1}".format(data, data_copy))


# Writing a For Loop
# writing Your First for Loop Using Range
# for num in range(5):
#     print("Value: {0}".format(num))


# Range()
# Providing the Start, Stop, and Step for the Range Function
# for num in range(2, 10, 2):
#     print("Value: {0}".format(num)) # Will Print All Evens Between 2 and 10


# Looping by Element
# Printing all Characters in a Name Using the 'in' Keyword
# name = "Sobhan Esmaeili"
# for letter in name:
#     print("Value: {0}".format(letter))


# Continue Statement
# using the Continue Statement Within a For Loop
# for num in range(5):
#     if num == 2:
#         continue
#     print(num)


# Break Statement
# Breaking out of a Loop Using the 'Break' Keyword
# for num in range(5):
#     if num == 3:
#         break
#     print(num)


# Pass Statement
# Setting a Placeholder Using the 'pass' Keyword
# for i in range(5):
#     # TODO: add code to print number
#     pass


# While Loops
# writing your first while loop
# health = 10
# while health > 0:
#     print(health)
#     health -= 1  # Forgetting This Line Will Result in Infinite Loop


# Infinite Loops
# state = False
# while not state:
#     print(state)


# Nested Loops
# Using two or More Loops Together is Called a Nested Loop
# for i in range(2):  # Outside Loop
#     for j in range(2): # Inside Loop
#         print(i, j)


# Working with Lists
# Checking Length
# checking the number of items within a list
# nums = [5, 10, 15]
# length = len(nums)  # len() Returns an Integer
# print(length)


# Slicing Lists
# accessing specific items of a list with slices
# nums = [5, 10, 15]
# print(nums[1:3])  # Will Output Items in Index 1 and 2
# print(nums[:2])  # Will Output Items in Index 0 and 1
# print(nums[::2])  # Will Print Every Other Index - 0, 2, 4, etc.
# print(nums[-2:])  # Will Output the Last two Items in List


