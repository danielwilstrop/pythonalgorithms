

#Helper function swaps numbers
def swap(arr, index_1, index_2):
  temp = arr[index_1]
  arr[index_1] = arr[index_2]
  arr[index_2] = temp
  
# define bubble_sort():
def bubble_sort(arr):
  for el in arr:
    for i in range(len(arr) - 1):
      if arr[i] > arr[i + 1]:
        swap(arr, i, i + 1)
  return arr


# Tests 
list_1 = [9,4,6,7,2,4,1,3]
list_2 = [1,2,4,5,6,10,7,3,8]

print(bubble_sort(list_1)) #prints [1, 2, 3, 4, 4, 6, 7, 9]
print(bubble_sort(list_2))  #prints [1, 2, 3, 4, 5, 6, 7, 8, 10]