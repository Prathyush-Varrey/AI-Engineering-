"""
Dictionary in python as a data structure are going to store 
the values in a similary way just like the general
dictionary
{
 "key" : value(value can be any thing)
}
Using key name we can access values 
"""

example_dict = {
    "Name" : "Shiva",
    "Email" : "shiva@gmail.com",
    "Mobile-Number" : 9201224567,
    "Qualification" : "BTech"
}

#print(example_dict["Name"])


#Methods
'''
keys() -> returns all of the keys present inside our dictionary
values() -> return all values present inside dictionary
items() -> returns the key value pair together from dictionary
get() -> returning the value for the key that passed inside get method
'''

#print(example_dict.keys())
#print(example_dict.values())

#print(example_dict.items())
#print(example_dict.get("Name"))

# copy() -> it shallow copies each and every key value pairs form the original, but if original dictionary got updated the copy dictionay will not get updated with new values

dict_1 = {
    "Name" : "Shiva",
    "Email" : "shiva@gmail.com",
    "Mobile-Number" : 9201224567,
    "Qualification" : "BTech"
}

dict_2 = dict_1.copy()
dict_1["Name"] = "Ram"
print(dict_2)

"""
Additional functions in a list are:
sum()
max()
min()
len()
"""