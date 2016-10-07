# functions and files

from sys import argv

script, input_file = argv # in console, enter this script name and the file you would ike to read!

def print_all(f): # defines a new function, print_all with the argument f
    print(f.read()) # read the whole file.

def rewind(f):  # defines function rewind, with argument f
    f.seek(0)   # moves us to file offset position 0, the start of file

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First, let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

# call print_a_line function three times, one for each line to print individually:
current_line = 1
print_a_line(current_line, current_file) # current_line = 1, argument line_count=current_line, f = current_file

current_line += 1 # replaced current_line = current_line + 1 with +=. this is like saying x = x + y is the same as x += y.
print_a_line(current_line, current_file) # current_line = 2

current_line += 1
print_a_line(current_line, current_file) # current_line = 3
