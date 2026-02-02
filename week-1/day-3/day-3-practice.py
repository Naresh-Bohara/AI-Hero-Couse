# ---------------------------- Homework / Practice ----------------------------------

'''
Task:
Create a program that asks for the user's name, age, and favorite
color. Then print a personalized message using all three formatting
methods.
'''

username = input("Please enter your Name: ")
age = int(input("Please enter your age: "))
favourite_color = input("Please enter your favourite color: ")

print()
print("--------using string concatenation (+) method-----------")
print("Hello "+ username + " you are "+str(age) +" years old, "+ "and your favourite color is "+favourite_color +".")
print()

print("--------using str.format() method-----------")
print("Hello {} you are {} years old and your favourite color is {}".format(username, age, favourite_color))
print()

# using % Operator method:
print("--------------using using % Operator method -----------------")
print("Hello %s your are %d years old and your favourite color is %s" %(username, age, favourite_color))
print()

print("-------using f-string formatting--------")
print(f"Hello! {username}, You are {age} years old and your favourite color is {favourite_color}.")
print()





