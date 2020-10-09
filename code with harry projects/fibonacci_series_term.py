# FIBONACCI SERIES

n=int(input("enter the nth term\n"))
def fibo(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

print("your ",n,"th term in the fibonacci series is:")
print(fibo(n))
