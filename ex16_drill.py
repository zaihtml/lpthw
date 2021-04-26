# this is an operation to read the file created in ex16 
from sys import argv

script, filename = argv

print "Type the filename:"
file_name = raw_input("> ")

txt_name = open(file_name)

print txt_name.read()