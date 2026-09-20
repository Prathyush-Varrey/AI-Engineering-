'''
SETS : its a Data Structure which store values inside
of curly braces {} , are know for storing the values which
are non duplicate         


'''
set_1 = {1,2,3,4,1,2,3}
print(set_1)

#Menthod
#add() -> going to be used in sets for inserting our values at last index
set_1.add(7)
print(set_1)

set_2 = {1,2,3,4,5}
for i in range(1, 50):
    if i%2 ==0:
        set_2.add(i)
print(set_2)