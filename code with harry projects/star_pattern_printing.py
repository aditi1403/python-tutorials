# PATTERN PRINTING (CODE 1)

print("Please enter the number of rows you want to print:\n")
one=int(input())
print("type 1 or 0:\n")
two=int(input())
new=bool(two)
if new==True:
    for i in range(1,one+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print()
elif new==False:
    for i in range(one,0,-1):
        for j in range(1,i+1):
            print("*",end="")
        print()

# PATTERN PRINTING (CODE2)

a=int(input("Please enter number of rows you want to print:\n"))
b=bool(int(input("please add 0 for False and 1 for True:\n")))

def star(a,b):
    if b==True:
        c=1
        while c<=a:
            print(c*"*")
            c+=1
    else:
        while a>0:
            print(a*"*")
            a-=1

star(a,b)
