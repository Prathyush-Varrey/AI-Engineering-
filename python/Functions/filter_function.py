'''
Filter function will return only those items which are meeting
a certain given condition in an iterable

syntax
list(filter(function, iterable))
'''

# return all even nums from list
def even_nums(nums):
    if nums % 2 ==0 :
        return True

nums = [1,2,3,4,5,6,7,8,9,10,11,23,24,28,31,32,36,33,96,101]

even_nums = list(filter(even_nums,nums))
print(even_nums)

find_even_nums = list(filter(lambda x : x%2==0, nums))
print(find_even_nums)