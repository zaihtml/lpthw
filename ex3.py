print "I will now count my chickens:"
# This line adds 25 to 30 divided by 6
print "Hens", 25 + 30 / 6
# This line multiplies 25 by 3 then finds the remainder of 75 divided by 4, which is 3, then takes it away from 100.
# % is like two sums in one. First you have to divide the left number by the right number.
# For example 3 % 4. First do 3 / 4. You get 0.75. Then multiply 4 by 0.75. You get 3, so your answer is 3.
print "Roosters", 100 - 25.0 * 3.0 % 4.0

print "Now I will count the eggs:"
# % and * have identical 'priority' but 'outrank' - so they must be carried out before the - operation
# this breaks down to (3 + 2 + 1) - 5 + (4 % 2) - (1 / 4) + 6
# then 6 - 5 + 0 + 0 + 6
# so 1 + 6 = 7
# 1/4 equals 0 here because of floating point numbers
print 3 + 2 + 1 - 5 + 4 % 2 - 1.0 / 4.0 + 6

print "Is it true that 3 + 2 < 5 - 7?"
# this operation evaluates whether the sum on the left is less than the sum on the right.
print 3 + 2 < 5 - 7
# these are simple operations. Does what it says on the tin.
print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's False."

print "How about some more."
# the < > <= >= characters will create an result that is 'true' or 'false' depending on the numbers/sums on either side.
# this looks at whether 5 is greater than -2
print "Is it greater?", 5 > -2
# this looks at whether 5 is greater than or equal to -2
print "Is it greater or equal?", 5 >= -2
# this looks at whether 5 is less than or equal to -2
print "Is it less or equal?", 5 <= -2