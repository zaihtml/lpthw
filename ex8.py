# this assigns a string to a variable
formatter = "%r %r %r %r"

# this is a list of prints using different data types
# type one is integers
print formatter % (1, 2, 3, 4)
# type two is strings
print formatter % ("one", "two", "three", "four")
# type three is booleans 
print formatter % (True, False, False, True)
# type four is a string constructed by the above variable 
print formatter % (formatter, formatter, formatter, formatter)
# type 5 is a list of strings within parentheses 
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)
# in terminal, the third line of this printed with double quotes instead of single like the others
# this is bc python prints things in the most efficient way it can
# not replicate exactly the way you wrote them
# this is fine since %r is used for debugging so is not meant to be pretty

# assigning %r to the variable at the start meant that each print line starting with 'formatter %'
# would print the items in the parentheses exactly as they appear
# i.e. the 'raw programmer's' version of variable, also known as the 'representation'.
