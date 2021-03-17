# prints a string
print "Mary had a little lamb."
# prints a string with a formatter
print "Its fleece was white as %s." % 'snow'
# prints a string
print "And everywhere that Mary went."
# prints ten full stops in a row
print "." * 10 # what'd that do?

# this is a sequence of variables being assigned letters
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# here the letters assigned above are printed as a single string
# watch that comma at the end. try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12
# the comma causes the the next print line to follow on the same line rather than on the next.
# you could turn these last two lines into one single-line print instead of using the comma
# but that would be longer than 80 characters which in Python is bad style