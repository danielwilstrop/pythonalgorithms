# Python Implemnentaion of a binary search algorithm
import math

def binary_search(list, item):
    low = 0
    high = len(list)

    while low <= high:
        mid = math.floor((low + high) / 2)
        attempt = list[mid]
        if attempt == item:
            return mid
        if attempt > item:
            high = mid -1
        else:
            low = mid + 1
    return None


#Tests 
list = [1,3,5,7,9]
print(binary_search(list, 3))  #returns 1

print(binary_search(list, -6))  #returns None