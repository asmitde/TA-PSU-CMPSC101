#################
# mymath module #
#################


# Add function
def add(num1, num2):
    sum = num1 + num2

    return sum

# Subtract function
def subtract(num1, num2):
    difference = num1 - num2

    return difference

# Multiply function
def multiply(num1, num2):
    product = num1 * num2

    return product

# Divide function
def divide(num1, num2):
    if num2 == 0:
        return None
    
    division = num1 / num2

    return division

# Prime check function
def isPrime(num):
    if num == 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True        

# Factorial function
def factorial(num):
   fact = 1
   for i in range(2, num + 1):
       fact *= i

   return fact