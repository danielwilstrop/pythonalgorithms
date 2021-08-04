# Super simple factorial algorithm using recursion

def factorial(i):
    if i == 1:
        return i
    else:
        return i * factorial(i - 1)

#Tests

print(factorial(5))  #Prints 120
print(factorial(20))  #Prints 2432902008176640000