# Here's some new strange stuff, remember type it exactly.

# a set of variables are being made here
# the first is a simple string
days = "Mon Tue Wed Thu Fri Sat Sun"
# the second is also a string but uses \n to begin a new line with each month 
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# this is a print which combines a unique string with a variable 
print "Here are the days: ", days
# this does the same 
print "Here are the months: ", months

# the triple quotes allow you to write as many lines as you want
# without having to put 'print' before each line 
# just remember to end it with another set of triple quotes
print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""