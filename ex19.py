# here, a function is being defined
# we are counting the number of cheeses and the number of crackers
# the number of cheeses and crackers are not defined within the function
# the number is assigned later in the script, within each of the four bits below 
# the variables assigned below the function do not change the variables within the function
# they are passed to the function and temporary versions are made
# just for the functions run
# when the functions exit, these versions go away and everything keeps working 
def cheese_and_crackers(cheese_count, box_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % box_of_crackers
	print "Man, that's enough for a party!"
	print "Get a blanket. \n"
	
# this line assigns numbers to the function in one line
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# this one uses variables to assign numbers to the function
# it'd be bad if the global variables below had the same name as the function variables
# because then you can get confused as to which you're talking about
# sometimes, necessity might mean you have to use the same name
# but this should be avoided 
print "OR we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# this one uses maths to assign numbers to the function
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# this one combines the variables with maths
# these variables work here because they are global variables
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# writing my own function here
def jam_and_toast(jars_of_jam, slices_of_toast):
	print "There are %d jars of jam." % jars_of_jam
	print "There are %d slices of toast." % slices_of_toast
	print "This is going to be a great breakfast."
	print "But what about \'second breakfast\'?\n"
	

jam_and_toast(6, 12)

number_of_jams = 3
number_of_toasts = 9
jam_and_toast(number_of_jams, number_of_toasts)

jam_and_toast(10 + 5, 6 * 5)

jam_and_toast(number_of_jams + 60, number_of_toasts * 12)

jam_and_toast(12 * 12, 800 / 2)
