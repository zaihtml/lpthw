from sys import argv

# this line originally only had 2 arguments, I added the last name 
script, user_name, last_name = argv
# I changed this prompt from '>'
prompt = '-->'

# I added the last_name argument to be used in this line
print "Hi %s %s, I'm the %s script." % (user_name, last_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)

# I haven't fully understood this and the last exercise so I'm going to come back to it 