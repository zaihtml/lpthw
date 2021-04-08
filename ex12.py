# for raw_input(), you can put in a prompt to show a person so he knows what to type
# put a string that you want for the prompt inside the () so it looks like:
# y = raw_input("Name?")

# the previous exercise can be rewritten completely

age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)