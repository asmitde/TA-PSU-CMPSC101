import mymath

#Enter two numbers
x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
print()

# Call the add function
resAdd = mymath.add(x, y)
print("Sum =", resAdd)

#Call the subtract function
resSub = mymath.subtract(x, y)
print("Difference =", resSub)

#Call the multiply function
resMul = mymath.multiply(x, y)
print("Product =", resMul)

#Call the divide function
resDiv = mymath.divide(x, y)
print("Division =", resDiv)
print()

#Call the isPrime function
resPri = mymath.isPrime(x)
if resPri == True:
    print(x,"is Prime")
else:
    print(x,"is not Prime")

#Call the factorial function
resFac = mymath.factorial(y)
print(y, "Factorial =", resFac)