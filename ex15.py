# this line calls an argument variable from the system
from sys import argv

# this line unpacks the argument variable
# when running in terminal, you have to type the name of this file,
# as well as the name of the file you want to open
script, filename = argv

# this assigns the command 'open' to the 'txt' variable 
txt = open(filename)

print "Here's your file %r:" % filename
# you give a file a command by using the full stop,
# the name of the command, and parameters
# when you say txt.read() it is like you are saying 
# 'Hey txt! Do your read command with no parameters.' 
print txt.read()
# this does the same thing but allows you to write in the file name via input 
print "Type the filename again:"
file_again = raw_input("> ")
# then a command is set to open the file which you inputted
txt_again = open(file_again)
# then this command tells the computer to 'read' or 'print' the contents 
print txt_again.read()

# you can open a file in one of two ways as shown in this file 
# you could use the way as shown in lines 7 - 17 
# or the way shown in lines 19 - 24 
# I prefer the second way mainly because I don't fully understand the first way 