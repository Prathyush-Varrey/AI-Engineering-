#Map()

'''
Map functions applies a given function operation to all items
in an iterable or a list and returns a map object  

'''

squared_list = list(map(lambda x:x**2, [1,2,3,4,5,6]))
print(squared_list)

def squared_nums(num):
    return num**2

squared_list2  = list(map(squared_nums,[1,2,3,4]))
print(squared_list2)

num1 = [1,2,3,4]
num2=[2,3,4,5]

print(list(map(lambda x,y:x+y, num1, num2)))