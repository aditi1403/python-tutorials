# SNAKE-WATER-GUN GAME

import random
draw_count=0
lost_count=0
win_count=0
number_of_guesses=1

print("This is a SNAKE-WATER-GUN game!! :)\n",
"and the competition is between you and me :}\n",
"so let's begin!!....SNAKE....WATER....GUN\n")

list=["snake","water","gun"]

while (number_of_guesses<=10):
    choice = random.choice(list)
    n = str(input("Enter your choice (snake/water/gun):\n"))
    print("Now my turn:",choice)
    if n=="snake" and choice=="water":
        print("You win! :) ...I lose! :(")
        win_count+=1
    elif n=="snake" and choice=="gun":
        print("I win! :) ...You lose! :(")
        lost_count+=1
    elif n=="snake" and choice=="snake":
        print("DRAW!")
        draw_count+=1
    elif n=="water" and choice=="gun":
        print("You win! :) ...I lose! :(")
        win_count+=1
    elif n=="water" and choice=="snake":
        print("I win! :) ...You lose! :(")
        lost_count+=1
    elif n=="water" and choice=="water":
        print("DRAW!")
        draw_count+=1
    elif n=="gun" and choice=="snake":
        print("You win! :) ...I lose! :(")
        win_count+=1
    elif n=="gun" and choice=="water":
        print("I win! :) ...You lose! :(")
        lost_count+=1
    elif n=="gun" and choice=="gun":
        print("DRAW!")
        draw_count+=1
    else:
        print("INVALID !! :(")
        break
    print("You have",10-number_of_guesses," chances left :)")
    number_of_guesses+=1

if number_of_guesses>10:
    print("The number of times:\n",
          "You WON:",win_count,"times\n",
          "You LOST:",lost_count,"times\n",
          "We had a DRAW:",draw_count,"times\n")
if lost_count>win_count:
    print("I WIN !!!")
elif lost_count<win_count:
    print("YOU WIN !!!")
else:
    print("IT'S A DRAW !!!")
