'''
Tuple : are 2nd type of da wich can store the data in a ordered way
jst like list but tuples are immutable
'''

a = tuple()
#print(type(a))

a1 = (1,2,3,4,5,"shiv",4.5,False)

#a1[1] = 5
#print(a1)
#for i in a1:
   # i = i *2
    #print(i)

#print(a1[1:])
#print(a1[::-1])

#methods -> only 2 1) count() 2) index() 

a2 = (1,2,3,4,5,6,2,2,1)

#print(a2.index(2)) returns 1st occurance of value
#print(a2.count(2))

'''
Packing and Unpacking of tuples:

'''
#packing
b1 = 1,2,3,4,5,12,123,"ram"
#print(type(b1))

#unpacking
b2,b3,b4,b5,b6,b7,b8 = (1,2,3,4,5,6,"ram")
#print(b8)

#unpacking with a *

first_value,*middle_value,final_value=(1,2,3,4,5,6,7,8,9,10)
#print(first_value)
#print(middle_value)
#print(final_value)


#Nested list
nested_list = [[1,2,3],[4,5,6],["prathyush",4.5,12],[1,42,33,12,2]]
#access
#print(nested_list[0][::-1])

#tuples in list
tup_lists =[(1,2,3),(2,3,4),(3,4,5)]
#print(tup_lists[0][0:])
nested_tup=((1,2,3),(2,3,4),(3,4,5))
for i in nested_tup:
    for j in i:
        print(j , end=" ")
    print(" ")

print("--------------")
#operation in tuple
tup1 = (1,2,3,4,5,6)
tup2 = (2,3,4,5,6,7)
print(tup1 + tup2)
print(tup1*10)