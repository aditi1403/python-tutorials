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

# f=open("file name")
# """opens a file"""

# f.close()
# """closes the opened file"""

# f.read()
# """reads the content in the file,
# can also specify the number of characters 
# you want to read"""

# for line in content:
#      print(line)
# """prints the entire content as
#  characters in a vertical line
#  like...a
#         b
#         c...this way :)"""

# for line in f:
#     print(line)
# """prints the entire text in lines
# as in the content like...
# this is first line
# 
# this is second line
# 
# this is third line...this way :)"""
# """these spaces are by default 
# in our content as the conten text is:
# this is first line
# this is second line
# this is third line"""

# for line in f:
#     print(line, end="")
# """this is the code to print the 
# content as we have written it """

# print(f.readline())
# """prints the first line of the content
# and if printed again...prints the second 
# line of the content and so on """

# print(f.readlines())
# """prints all the lines of the text as:
# ["this is first line\n","this is second line\n","this is third line\n"]""""

# print(f.tell())
#tells the character number
# where our cursor is

# print(f.seek())
#navigates our cursor/pointer
# to the desired character
# number which we have entered
 
# # to open a file using 'with'
# the syntax for the same is;
 
# with open("file name") as f:
# 
# this syntax works the same as;
# 
# f=open("file name")
# f.close()
 
