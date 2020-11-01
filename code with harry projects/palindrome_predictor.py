# a palindrome is a string which when reversed is equal to itself:
# examples of palindrome includes 616, mom, 676,100001
# you have to take a number as an input from the user . you have to find the next palindrome number
# your first input should be"number of test cses
# and then take all the cases as input from the user

# input:
# *3
# *451
# *10
# *2133

# output:
# *next palindrome for 451 is 454
# *next palindrome for 10 is 11
# *next palindrome for 2133 is 2222
def next_palindrome(n):
    n=n+1
    while not is_palindrome(n):
        n+=1
    return n

def is_palindrome(n):
    return str(n)==str(n)[::-1]

if __name__=="__main__":
    n=int(input("enter the number of test cases:\n"))
    numbers=[]

    for i in range(n):
        number=int(input("enter the number\n"))
        numbers.append(number)
# print(numbers)
    for i in range(n):
        print(f"next palindrome for {numbers[i]} is {next_palindrome(number)}")
