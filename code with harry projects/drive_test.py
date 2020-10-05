#this is a driving liscence test
age=int(input("Enter your age:"))
if age>18 and age<120:
    print("you can drive :)")
elif age==18:
    print("cannot decide :/")
elif age>1 and age<18:
    print("too young to drive :(")
else:
    print("enter a valid age :?")
