
def merge_sort(items):
  if len(items) <= 1:
    return items

  middle_index = len(items) // 2
  left_split = items[:middle_index]
  right_split = items[middle_index:]
  
  #Recursion
  left_sorted = merge_sort(left_split)
  right_sorted = merge_sort(right_split)

  return merge(left_sorted, right_sorted)

#Merges the two lists together 
def merge(left, right):
  result = []
  while (left and right):
    if left[0] < right[0]:
      result.append(left[0])
      left.pop(0)
    else:
      result.append(right[0])
      right.pop(0)
  if left:
    result += left
  if right:
    result += right
  return result

#Tests 
list_1 = [356, 746, 264, 569, 949, 895, 125, 455]
list_2 = [787, 677, 391, 318, 543, 717, 180, 113, 795]

print(merge_sort(list_1)) #Prints [125, 264, 356, 455, 569, 746, 895, 949]
print(merge_sort(list_2)) #Prints [113, 180, 318, 391, 543, 677, 717, 787, 795]