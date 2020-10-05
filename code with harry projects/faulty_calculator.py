#FAULTY CALCULATOR
#wrong calculations:45*3=555,56+9=77,56/6=4
n=int(input("enter your first number:"))
m=int(input("enter your second number:"))
a=str(input("enter the operation you"
            " want to perform:"))

if n==56 and m==9 and a=="+":
    print("your sum is:77")
elif a =="+":
    print("your sum is:",n+m)
elif a =="-":
    print("your answer is:",n-m)
elif n==45 and m==3 and a=="*":
    print("your product is:555")
elif a =="*":
    print("your product is:",n*m)
elif n == 56 and m == 6 and a == "/":
    print("your answer is:4")
elif a =="/":
    print("your answer is:",n/m)
else:
    print("invalid input")
