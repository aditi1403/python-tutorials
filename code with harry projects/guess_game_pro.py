# you and your friend have to guess a number betweentwo numbers a and b are
# inputs taken fro the user . your friend is player 1  and plays first.
# he will have to keep choosing the number and you program must tell whether
# the number is greater than the actual number or less than the actual number .
# log the number of trials your friend to arrive at the number .
# you play the same game and thn the person with minimum trials wins!



##randomly generate a number and dont show that to the user (say6)

# input:
# enter the value of a
# 4
# enter the value of b
# 13
# ouput:

# player 1:
# please guess the number between 4 and 13
# 5
# wrong guess a greater number again
# 8
# wrong guess a smaller number again
# 6
# correct you took 3 trials to guess the number
# player 2:
# .
# .
# .
# correct you took 7 trials to guess the number

# PLAYER 1 WINS!!

import random
def guessgame(a,b,actual):
    guess=int(input(f"guess a number between {a} and {b}\n"))
    nguess=1
    while guess != actual:
        if guess< actual:
            guess=int(input(f"enter a bigger number\n"))
            nguess+=1
        else:
            guess=int(input(f"enter a smaller number\n"))
            nguess+=1
    print(f"you guesses the number in {nguess} guess\n")
    return nguess
if __name__=="__main__":
    a=int(input("enter the value a:\n"))
    b=int(input("enter the value b:\n"))
    actual=random.randint(a,b)
    print("player 1's turn:\n")
    g1=guessgame(a,b,actual)
    print("player 2's turn\n")
    actual2=random.randint(a,b)
    g2=guessgame(a,b,actual)
    if g1<g2:
        print("player 1 won the match\n")
    elif g1>g2:
        print("player 2 won the match\n")
    else:
        print("its a tie!!\n")


