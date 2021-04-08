# this first line is called an 'import'
# this is how you add features to your script from the Python feature set
# argv means 'argument variable'. This 'hold' the arguments to pass to your Python script when you run it
from sys import argv

ex13, citrus, berry, other = argv

print "The script is called:", ex13
print "Your first variable is:", citrus
print "Your second variable is:", berry 
print "Your third variable is:", other

# 'features' are actually called 'modules'
# a module is the same as a code library
# this is a file containing a set of functions you want to include in your application
# to create a module just save the code you want in a file with the extension '.py'
# you can call the module by using 'import' and the name of the file, as above