#Quicksort Implementaions with Python
import random

# with random index
def quicksort(arr): 
    if (len(arr) <= 1):
        return arr
    else:
        grt_arr = []
        less_arr = []
        rand_indx = random.randint(0,len(arr)-1)    
        pivot = arr[rand_indx] # picking up a random index
        for ele in (arr[0:rand_indx]+arr[rand_indx+1:]):
            if (ele <= pivot):
                less_arr.append(ele)
            elif (ele > pivot):
                grt_arr.append(ele)

    return quicksort(less_arr)+[pivot]+quicksort(grt_arr)


#Without random pivot
def quicksort1(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)
        
#Tests
print(quicksort([34,56,2,3,45])) #Prints [2, 3, 34, 45, 56]
print(quicksort(['jas', 'becka', 'dan', 'alice'])) #Prints ['alice', 'becka', 'dan', 'jas']
