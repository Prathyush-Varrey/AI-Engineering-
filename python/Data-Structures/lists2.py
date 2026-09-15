#this file contains list methods and list-comprehension

nums = [24, 11,12,1,2,3,4,5,6,7]

#original nums list
print(nums)
#list Methods
#append() -> inserts a value at end of list
nums.append(8)
print()
print(nums)


#insert() -> inserts a value in specific index, starting default
nums.insert(3,24)
print()
print(nums)


#remove ->  it removes th first occurance of the value/item given 
nums.remove(24)
print()
print(nums)
nums.insert(3,24)

#pop() -> removes values/items at specific index
nums.pop(0)
print()
print(nums)

#index() -> returns the index value of the values/items 
print(nums.index(2))

for i in range(3):
    nums.append(9)

#print(nums)

#count()-> returns num of repetations of the given specific value
print(nums.count(9))

#sort() -> helps to sort values in ascending order
nums.sort()
print(nums)

#revers() -> 
nums.reverse()
print(nums)

#clear() -> clears all values in list
nums2 = [1,2,34,421,12]
nums2.clear()
print(nums2)

#enumerate() -> helps us with getting the index value and along with actual value
nums1 = [1,2,3,5,4,6,7,9]
for index_val, item_val in enumerate(nums1):
    print(index_val, ":", item_val)

#len() -> returns length of list (returns tot num of items in list) 
print(len(nums1))

#list comprehension
#create a list storing the values from 0 to 100
#syntax -> [expression for item in iterable if condition]
#expression -> what we want to print
#for item in iterable -> looping statement
# if condition -> conditional statement

list_items = [x for x in range(1, 51)]
print(list_items)