#FILE IO BASICS_CONTINUED

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
