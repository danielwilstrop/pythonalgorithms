#Quicksort Implementaions with Python

import random

def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        #This line always chooses a randow index of the array/sub-array as the pivot to improve the runtime
        pivot = array[random.randint(0, len(array) -1)]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)
        

#Tests
print(quicksort([34,56,2,3,45])) #Prints [2, 3, 34, 45, 56]
print(quicksort([10,9,8,7,6,5,4,3,2,1,0])) #Prints [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
