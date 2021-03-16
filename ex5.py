name = 'Zainab Dawood'
age = 24 # not a lie
height = 64 # inches
# here I am adding a variable to convert inches to centimetres
height_cm = height * 2.54
weight = 140 # lbs
# here I am adding a variable to convert lbs to kilos
weight_kg = weight / 2.205
eyes = 'Brown'
teeth = 'White'
hair = 'Dark Brown'


print "Let's talk about %s." % name
print "She's %d inches tall." % height
print "In centimetres that's %f centimetres tall." % height_cm
print "She's %d pounds heavy." % weight
print "In kilos that's %f kilograms." % weight_kg
print "Actually that's not too heavy."
print "She's got %s eyes and %s hair." % (eyes, hair)
print "Her teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
	age, height, weight, age + height + weight)
	
# the %r format character prints the quotation marks along with the content of the string

# the %f format character prints the number as a floating point number (a number with a decimal point)
