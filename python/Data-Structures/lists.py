'''
lists : same as (Arrays)
are one of the type of data structure which are used fr storing your 
data in a structured format where you can store data of any data type
as it is one of the ds so we can hace access to the data as well that we 
are going to store into the list and can apply CRUD operations as well.

lists are ordered abd mutuable data structure
'''
a = list()

#print(type(a))

my_list = [1,2,3,4,5]

#print(my_list)

#list indexing -> 0 to length -1 len of the ds is going to be num of values in the ds

#print(my_list[0])
#print(my_list[len(my_list)-2])

lists = ["mango", "apple",'banana', 'guava','grapes','pineapple']

#print(lists[5])
#print(lists[2])

#negative indexing
#print(lists[-1])

# Slincing -> list_name[start_index: stop_index : step]
#print(lists[0:])

# reverse order
#print(lists[::-1])

#changing data using indexing
lists[4] = "papaya"
print()
#print(lists)

#iterating through loops

for items in lists:
    print(items)

nums = [1,2,3,4,5,6,7,8,9]

print(nums[::1])