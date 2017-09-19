# Script to get the nth Fibonacci number

# Fibonacci function definition
def fibonacci(num):
    a = 1
    b = 1

    if num < 3:
        return a

    for i in range(3, num +  1):
        c = a + b
        a = b
        b = c

    return c
# -- Function definition ends


# Take input
num = int(input("Enter a number: "))

# Call fibonacci function
f = fibonacci(num)

# Print result
print("\nFibonacci =", f)