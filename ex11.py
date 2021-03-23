# Most of what software does is the following
# 1. Take some kind of input from a person
# 2. Change it
# 3. Print out something to show how it changed

# this exercise is different from the previous ones
# because it requires input in the Terminal

# printing a question in a string 
print "How old are you?",
# the raw_input function gets input from the user and returns the data input by a user in a string 
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

# here a string is printed using formatters
# the formatters will be replaced by the user's input 
print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)
	
# note: we put a comma at the end of each print line.
# This is so that print doesn't end the line with a new line character and go to the next line.
