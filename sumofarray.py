# Add all values of an array using recursion

def sum(arr):
    if arr == []:
        return 0
    else:
        return arr[0] + sum(arr[1:])


# Recursive funtion to count length of a list, a copy of the built in Len() function
def len_of_list(arr):
    if arr == []:
        return 0
    else:
        return 1 + len_of_list(arr[1:])


#Tests
print(sum([1,2,3,4,5]))  #Prints 15
print(len_of_list([1,2,3,4,5]))  #Prints 15