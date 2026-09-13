#Operators : helps in applying operations on the given operands

'''
Types of Operators:
1) Arithmetic Operators: +, -, *, /, %, Floor(//), Exponent (a ** b)

2) Comparison Operators: 
    Greater than (>),
    Less than (<)
    Greater than or equal too (>=)
    Less than or equal too (<=)
    Equality check (==) check weather 2 values are equal or not 
    not equal to (!=) returns boolean

3) logical Operators:
    and -> if both conditions ture or not
    or -> any of the condition ia true or not 
    not -> negation operation or inverse the operation
'''
#arithmetic operations
a = 10
b = 22
print("arithmetic operations : ")
print("Addtion: ",a + b)
print("Substration: ",a - b)
print("Multiplication: ",a * b)
print("Division: ",a / b)
print("Modlus: ",a % b)
print("Floor: ",a // b)
c = 2
d = 5
print("Exponent: ",c ** d)


# comparison operations
print()
print("comparison operations : ")
print("Greater Than: ",a > b)
print("Less Than: ",a < b)
print("Greater Than Equal to: ",a >= b)
print("Less Than Equal to: ",a <= b)
print("Equality Check: ",a == b)
print("Not Equal to: ",a != b)

#logical operations
print()
print("logical operations: ")
print("And: ",a > d and b < c)
print("Or: ",a > d or b > c)
print("not: ",   not b ) 