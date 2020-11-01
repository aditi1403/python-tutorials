# you are given a list which contain some numbers. you have to
# print a list of next palindromes only if the number is greater
# than 10  otherwise you will print number.

# input:
# [1,6,87,43]

# output:
# [1,6,88,44]
def next_palindrome(n):
    n=n+1
    while not is_palindrome(n):
        n+=1
    return n
def is_palindrome(n):
    return str(n)==str(n)[::-1]

if __name__=="__main__":
    size=int(input("enter the size of your list\n"))
    num_list=[]
    for i in range(size):
        num_list.append(int(input("enter the number of the list\n")))
    print(f"you have entered {num_list}")

    print(f"output list: {[num_list[i] if num_list[i]<10 else next_palindrome(num_list[i]) for i in range(size)]}")

    # new_list[]
    # for element in num_list:
    #     if element >10:
    #         n=next_palindrome(element)
    #         new_list.append()
    #
    #     else:
    #         new_list.append(element)
    # print(f"output list: {new_list}")

