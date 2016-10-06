print "I am 6'2\" tall."  # escape double-quote inside string
print 'I am 6\'2" tall.'  # escape single-quote inside string

tabby_cat = "\tI'm tabbed in." #/t will tab in your string
persian_cat = "I'm split \non a line." # \n will create a line break in your string
backslash_cat = "I'm \\ a \\ %s." # \\ will print one \
r_cat = "I'm a %r."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
# \n\t is another way to make a line break and then a tab in the string


print tabby_cat
print persian_cat
print backslash_cat % 'cat'
print r_cat % 'cat' # note the difference between %r and %s
print fat_cat


# something else to try out:

while True: #print this forever.
    for i in ["/","-","|","\\","|"]: #makes list of characters: / - | \ |
        print "%s\r" % i,
