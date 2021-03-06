from random import randrange, shuffle

def quicksort(list, start, end):
  # this portion of list has been sorted
  if start >= end:
    return

  # select random element to be pivot
  pivot_index = randrange(start, end + 1)
  pivot_element = list[pivot_index]

  # swap random element with last element in sub-lists
  list[end], list[pivot_index] = list[pivot_index], list[end]

  # tracks all elements which should be to left (lesser than) pivot
  less_than_pointer = start
  
  for i in range(start, end):
    # we found an element out of place
    if list[i] < pivot_element:
      # swap element to the right-most portion of lesser elements
      list[i], list[less_than_pointer] = list[less_than_pointer], list[i]
      # tally that we have one more lesser element
      less_than_pointer += 1
  # move pivot element to the right-most portion of lesser elements
  list[end], list[less_than_pointer] = list[less_than_pointer], list[end]
  # recursively sort left and right sub-lists
  quicksort(list, start, less_than_pointer - 1)
  quicksort(list, less_than_pointer + 1, end)


    
#Tests  
list = [1,2,3,4,5,6,7,8,9,10]
shuffle(list)
print(list)
quicksort(list, 0, len(list) -1)
print(list)
