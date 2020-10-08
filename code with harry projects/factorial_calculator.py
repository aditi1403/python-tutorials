# FACTORIAL CALCULATOR

n=int(input("enter the number:\n"))
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
print("the factorial of",n,"is:",factorial(n))
