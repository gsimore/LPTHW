my_name = 'Gabrielle E Simard-Moore'
my_age = 22
my_height = 62 # inches
my_weight = 135 # pounds
my_eyes = 'Blue/Green'
my_teeth = 'White'
my_hair = 'Dirty Blonde'

print "Let's talk about %s" % my_name
print "She's %d inches tall" % my_height
print "She's %d pounds heavy" % my_weight
print "Actually, that's not too heavy."
print "She's got %s eyes and %s hair." % (my_eyes, my_hair)
print "Her teeth are usually %s, depending on the coffee" % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d, I get %d" % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)
