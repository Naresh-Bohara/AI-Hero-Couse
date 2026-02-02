### ----------- String Concatenation and String Formatting Methods ----------------

## String Concatenation:
# The + operator combines strings together, a process called concatenation. 
# This is one way to build complex text output in our programs.

# Using + Operator:
# first = "AI"
# second = "World"
# print(first + " " + second)

# ->  + joins strings only

# Numbers Must Be Converted:
# num = 10
# print("Number: " + str(num))  # ✅
# print("Number: " + num)       # ❌ Error
# Python does NOT auto-convert numbers to strings.

## String Formatting Methods:
# 1. f-strings 
# Introduced in Python 3.6, f-strings are the clearest, most readable way to format strings

# name = "Naresh"
# score = 93
# print(f"{name} scored {score} points")

# Advantages:
# - Clean
# - Readable
# - Fast
# - Expression support

# print(f"{name} needs {100 - score} more points")

# 2. str.format():
# print("{} scored {}".format("Naresh", 88))
# print("{1} scored {0}".format(88, "Naresh"))
# print("{}".format("Hello"))


# 3. % Formatting:
# print("%s scored %d" % ("Rohan", 92))
# print("%.2f percent" % 92.5)

# Working with User Data:
name = input("Please enter your Name: ")
age = int(input("Enter your age: "))

print(f"Hello!, {name}, you are {age} years old.")

import datetime
current_year = datetime.datetime.now().year
birth_year = current_year - age
print(f"{name} were born around {birth_year}. ")