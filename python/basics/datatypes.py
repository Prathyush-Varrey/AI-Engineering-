# data_types =  is a classification of data that tells the compiler
# or the interpreter that what kind of values we can store into a 
# vatiable and how much amt of memory will be consumed to store the data

#Numeric (int, float, complex)Used for math and counts.
age = 24
pi = 3.14
complex = 2+3j

#text (str) Immutable sequence of characters.
name = "prathyush"

#sequence (list , tuple, range) Ordered collections of items.
my_list = [1,2,3]
my_tuple = (1,23)

#mapping (dict)Key-value pairs for fast lookups
user_data ={
    "user_name" : "Prathyush",
    "user_age" : 25
}

#set tyoes (set, frozenset)Unordered collections of unique items.
my_set ={1,2,3}

#boolean (bool)Evaluates logic and conditions.
isTrue = True
isFalse = False

#binary (bytes, bytearray. memoryview)Handles raw binary packet data

#None (NoneType)Represents the absence of a value.

'''
Mutual Types (values can be changed): list ,dict ,set ,bytearray

Immutable Types(Cannot be alterd): int, float, complex, str, 
tuple, range, frozenset, bytes
'''