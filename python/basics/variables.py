# variable is a container that stores values (data)


user_name = "Prathyush"
user_age = 25
user_height = 5.7
is_user_Online = False

#print() -> prints data on console screen
print(user_age)

print("User Name is :", user_name)
print("User Age is :", user_age)
print("User Height is :", user_height)
print("User Online or Offline :", is_user_Online)

#naming conventions 
"""
variable name must be descriptive 
They must start with a letter or underscore and can contain letter,
numbers and underscores.
variables are case sensitive means it should only use small letters
Value can be Typecasted (from int <-> boolean or anyother data type)
str to int can't be typecasted
"""

#input() -> used to take input from user
num1 = int(input("Enter  a number Num 1: "))
num2 = int(input("Enter  a number Num 2: "))
#add
print(num1 + num2)