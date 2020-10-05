#GUESS GAME
n=20
number_of_guesses=1
print("this is a guess game !!...hope you enjoy it... :)")
print("number of guesses is only limited to 9... ;)\n")
while(number_of_guesses<=9):
    guess_number=int(input("guess the number:\n"))
    if guess_number>20:
        print("guess a little less... :}\n")
    elif guess_number<20:
        print("guess a little more... :}\n")
    else:
        print("you won!! :)")
        print("you took",number_of_guesses,
              "guesses to finish the game :)")
        break
    print(9-number_of_guesses,"guesses left... :}")
    number_of_guesses=number_of_guesses+1
if number_of_guesses>9:
    print("oops!you are out of guesses... :(")
    print("GAME OVER!!")
