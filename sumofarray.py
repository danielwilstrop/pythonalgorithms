# Add all values of an array using recursion

def sum(arr):
    if arr == []:
        return 0
    else:
        return arr[0] + sum(arr[1:])


#Tests
print(sum([1,2,3,4,5]))  #Prints 15