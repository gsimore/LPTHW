from sys import argv
from os.path import exists

script, from_file, to_file, = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these on one line... How?
in_file = open(from_file) # maybe by passing 'r' as a second parameter in open() ?
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()

txt_from = open(from_file, 'r')

print "Here is the original file you copied from: %r" % from_file
print txt_from.read()

txt_to = open(to_file, 'r')

print "And here is your new file: %r" % to_file
print txt_to.read()
