# Prompts!!

y = raw_input("Name? ") # The string entered in the parentheses is your prompt message. So, we could change files ex11.py and ex11b.py into using this format rather than using print before the variable

age = raw_input("How old are you?")
height = raw_input("How tall are you?")
weight = raw_input("How much do you weigh?")

print "So %r, you're %r old, %r tall, and %r heavy." % (
    y, age, height, weight)

# just learned pydoc.
# to use pydoc, type pydoc in terminal followed by any python word, term or keyword to search documentation.
# example: pydoc raw_input
