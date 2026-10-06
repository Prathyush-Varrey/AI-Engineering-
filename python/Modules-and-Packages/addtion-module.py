


nums = (1,2,3,4,5,6,7,8,9,10)
 

from packge_folder.calculations import *

print(addtion(*nums))
print(subtraction(*nums))
print(multiplication(*nums))

"""
Standard Libraries in python

Python Standard Libraries is a vast collection of Modules and Packages
that come bundled with python and it provides us with a vast range of
functionalities

"""
from math import *

print(round(sqrt(4)))

import random
print(random.randint(1,200))

import csv

with open("example1.txt", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'age'])
    writer.writerow(['Bhanu', '26'])

with open('example1.txt', mode='r')as file:
    reader = csv.reader(file)
    for i in reader:
        print(i)

from datetime import *

current_time = datetime.now()

print(current_time-timedelta(days=2))

