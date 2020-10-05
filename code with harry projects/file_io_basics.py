# File IO Basics


# """
# "r"-open file for reading-default
# "w"-open a file for writing
# "x"- create file is not exists
# "a"-add more content to a file
# "t"-text mode-defaut
# "b"-binary mode
# "+"-read and write
# """

# How to write in a file
# f=open("file name","w")
# """w means write"""
# a=f.write("text you want to enter\n")
# print(a)
# f.close()

# how to append a file
# f=open("file name","a")
# """a means append"""
# a=f.write("text you want to enter\n")
# print(a)
# f.close()

# Handle read and write both
# f=open("file name","r+")
# """r+ means both read and write"""
# print(f.read())
# f.write("text you want to write")
