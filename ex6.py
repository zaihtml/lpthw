# the %d is replaced by 10, because '% 10' is written after the string
x = "There are %d types of people." % 10
# the variable is issued a string
binary = "binary"
# the variable is issued a string
do_not = "don't"
# a new variable is created, the string of which uses the previous variables (and their assigned strings)
# a string is put inside a string (twice)
y = "Those who know %s and those who %s." % (binary, do_not)

# the first variable (the setup) is printed
print x
# the fourth variable (the punchline) is printed
print y

# A string is printed with %r and using the first variable, meaning that it will be printe with quote marks around it.
# a string is put inside a string
print "I said: %r." % x
# A second string is printed in the same way but with a %s instead of a %r, but the %s has quotes around it, garnering the same result.
# a string is put inside a string
print "I also said: '%s'." % y

# this variable is assigned a boolean value (learn about this later)
hilarious = False
# this variable string uses %r but does not have anything written after the string to assign to it, yet it works.
# not sure why, maybe it's because it automatically uses the most recent variable?
joke_evaluation = "Isn't that joke so funny?! %r"

# I thought the % here could be replaced by a '+' but it can't.
# the error said 'TypeError: cannot concatenate 'str' and 'bool' objects.'
print joke_evaluation % hilarious

# the variable is assigned a string
w = "This is the left side of..."
# the variable is assigned a string
e = "a string with a right side."

# the strings are added together to create a new string which is printed
# this creates a new string because only the stuff inside the quote marks are printed so it looks like a whole sentence or new string
print w + e