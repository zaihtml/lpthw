# the first variable contains an escape which 'tabs' the string 
tabby_cat = "\tI'm tabbed in."
# the second variable contains an escape which splits the string on a new line
persian_cat = "I'm split\non a line."
# the third variable contains two backslashes entered via an escape sequence 
backslash_cat = "I'm \\ a \\ cat."

# This variable is split over four lines using triple double-quotes
# it also contains the escape sequence for tab three times
# replacing the double-quotes with single-quotes doesn't seem to make a difference
# I'm not sure why you'd use one rather than the other
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# Here's a tiny piece of fun code to try out (remove the hashes and the space to work)
# while True:
	# for i in ["/","_","|","\\","|"]:
		# print "%s\r" % i,

# "The quick brown fox jumps over the lazy dog"
# the first time I tried this I missed out the '%' after the string
# so I got this error: 'TypeError: 'str' object is not callable'
# I added single and double quote escapes to the variable strings
# then I added %r and %s formatters into the string to see what would happen
# I swapped and played around with this a few times to see the different variations

fox = "\'fox\'"
dog = "\"dog\""

print "The quick brown %r jumps over the lazy %r." % (fox, dog)
