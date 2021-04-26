# sys is a package, and this phrase means to get the argv feature from that package
from sys import argv

# assigning the files to argv...
script, filename = argv

# printing lines to show what is going to happen
print "We are going to erase %r." % filename 
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

# a question mark appears to indicate you should enter some input here
raw_input("?")

# a printed line to indicate what is happening by the line below 
print "Opening the file..."
# this assigns the word 'target' to a command.
# 'w' is really a string with a character for the mode of the file 
# 'w' means 'open this file in write mode'
# there's also 'r' for read and 'a' for append
target = open(filename, 'w')

# this orders the truncation of the target file, as defined above
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines..."

# the lines are assigned raw input strings 
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# the 'write('x')' operation writes stuff to the file 
target.write(line1)
target.write("/n")
target.write(line2)
target.write("/n")
target.write(line3)
target.write("/n")

# this operation closes the file 
print "And finally, we close it."
target.close()