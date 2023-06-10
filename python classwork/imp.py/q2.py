n = int(input("enter the number to find its factorial : "))
fact = 1
while (n>0) :
    fact = fact*n
    n = n-1

print("factorial of the number is :", fact)