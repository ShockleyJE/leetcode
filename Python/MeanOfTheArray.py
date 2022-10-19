from functools import reduce
from math import floor


def get_average(marks):
    total = reduce(lambda x,y: x+y, marks, 0)
    average = floor(total/len(marks))
    return average


print(f" Average should be: 2  Is: {get_average([2,2,2,2])}")
print(f" Average should be: 3  Is: {get_average([1,2,3,4,5,])}")
print(f" Average should be: 1  Is: {get_average([1,1,1,1,1,1,1,2])}")