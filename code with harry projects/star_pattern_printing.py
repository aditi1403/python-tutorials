# PATTERN PRINTING (CODE 1)

print("how many row you want to print:\n")
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

a=int(input("please enter number of lines you want to print"))
b=bool(int(input("please add 0 for False")))

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
