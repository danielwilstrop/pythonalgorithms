#Implementaion of selection sort using python

# Util function to find the smallest item in an array and return its index
def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest_index = i
    return smallest_index


def selection_sort(arr):
    sorted_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        sorted_arr.append(arr.pop(smallest))
    return sorted_arr


# Tests
print(selection_sort([3,6,31,20,17,1]))  #Prints [1, 3, 6, 17, 20, 31]
print(selection_sort([100,90,80,70,60,50])) #Prints [50, 60, 70, 80, 90, 100]




