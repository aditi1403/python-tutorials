#* YOUR AGE IN 2090

# take age or year or birth as an input from the user and
# tell them when will they turn 100 years old.(5 points)
# don't use any type of modules like datetime or datedetails.
# (-5 points)
# they can then optionally provide a year and your program
# must tell their age in that particular year.(3 points)

# you should be handling all sorts of errors like(2 points):
#* you are not yet born
#* you seem to be the oldest person alive
#* you can also handle any other error if possible

x=int(input("what is your age/year of birth"))
age=False
year=False

if len(str(x))==4:
    year=True
if x<125:
    age=True

elif x>1900:
    year=True
else:
    print("there was some problem with your age/year of birth")
    exit()
if (x<1900 and year):
    print("you seem to be the oldest person on this planet alive")
    exit()
if x>2020:
    print("you are not yet born")
    exit()

if age:
    x=2020-x
print(f"you will be 100 years old in {x+100}")
