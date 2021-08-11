#Quicksort Implementaions with Python
import random

def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        random_index = random.randint(0, len(array) -1)
        pivot = array[random_index]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)
        
#Tests
print(quicksort([34,56,2,3,45])) #Prints [2, 3, 34, 45, 56]
print(quicksort(['jas', 'becka', 'dan', 'alice'])) #Prints ['alice', 'becka', 'dan', 'jas']
