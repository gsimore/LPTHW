#printing, printing, printing

# here's some new strange stuff. Remember to type it exactly

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\n%s" #use \n to create a line break!

print "Here are the days:", days
print "Here are the months:", months % "Sep\nOct\nNov\nDec" # note that \n does not work inside of %r, but works with %s

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""
