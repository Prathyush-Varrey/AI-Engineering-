# Lambda Functions

"""
Lambda functions are the one liner functions
"""


#syntax for lambda function:
# lambda arguments : expression

#sum of 2 nums using lambda fun
sum = lambda x,y: x+ y

print(sum(2,2))

# square 
square = lambda x : x**2

print(square(10))

#power 
power = lambda number, power_num : number ** power_num

print(power(10,2))