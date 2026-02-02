# ---------------------- Day 03 — Input, Output in Python -----------------------
# 1. Input & Output Basics:
## What is Output?
# Output means displaying information from your program to the user.
# In Python, output is mainly handled using:
        # print()

### Used for:
# - Showing results
# - Debugging
# - User interaction
# - Logging (basic level)

### What is Input?
# Input means taking data from the user while the program is running.

# In Python:
#         input() is used to take input from keyboard

###---------------- Used for ------------:
# - Interactive programs
# - Forms
# - User-driven logic

### --------------- Interactive Programs -----------------
## An interactive program:
# - Asks the user for data
# - Processes it
# - Shows meaningful output

## Example flow:
# Ask → Receive → Process → Display

### This is the foundation of:
# - CLI tools
# - Backend APIs (conceptually)
# - AI applications (data in → result out)


# 2. The print() Function:
# Basic Printing
# print("Hello World")
# print(100)
# print(3.14)

# Can print:
# Strings, Numbers, Variables, Expressions

# Printing Variables:
# x = 5
# print(x)
# print("Value of x is", x)
# Python automatically adds space when using commas.

### Printing Multiple Values
# name = "Alice"
# age = 20
# print("Name:", name, "Age:", age)

    ### Escape Characters (Formatting Output)
    # Escape	Meaning
    # \n	    New line
    # \t	    Tab space
    # \\	    Backslash

# print("Line 1\nLine 2")
# print("Name:\tPython")

# 3. The input() Function:
# Taking User Input
# name = input("Enter your name: ")
# print(name)

#  - Input Always Returns str
# age = input("Enter age: ")
# print(type(age))  # <class 'str'>

### Type Conversion with Input
age = int(input("Enter age: "))
height = float(input("Enter height: "))
print("Next year you will be", age + 1)