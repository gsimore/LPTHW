#python3
# functions and variables

def cheese_and_crackers(cheese_count, boxes_of_crackers): # we give the function two arguments; cheese_count and boxes_of_crackers
    print("You have {} cheeses!" .format(cheese_count))
    print("You have {} boxes of crackers!" .format(boxes_of_crackers))
    print("Man that's enough for a party!")
    print("Get a blanket. \n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30) # we are assigning numbers to the two arguments: cheese_count and boxes_of_crackers, respectively, as they are defined in the intial function

print("OR, we can use variables from our script:")
amount_of_cheese = 10 # make new argument variables
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers) # assign these new variables to cheese_count and boxes_of_crackers

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6) # okay, we're calculating what cheese_count and boxes_of_crackers are right here.

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) # very cool.
