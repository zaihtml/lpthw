# each line below is an example of a variable. A number is assigned as the value of each variable name.
cars = 100
# a floating point number is used in this one but it doesn't really need to be.
space_in_a_car = 4.0
# there have to be fewer drivers than cars for this to work
drivers = 30
# there are 90 passengers
passengers = 90
# a variable can be assigned the sum of two other variables
cars_not_driven = cars - drivers
# a variable can have the same value as another variable
cars_driven = drivers
# another example where a variable is assigned the sum of two other variables
carpool_capacity = cars_driven * space_in_a_car
# another example where a variable is assigned the sum of two other variables
average_passengers_per_car = passengers / cars_driven

# These lines combine the variables with strings
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."