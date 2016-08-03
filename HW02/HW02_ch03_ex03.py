#!/usr/bin/env python
# HW02_ch03_ex03

# This exercise can be done using only the statements and other features we 
# have learned so far.

# (1) Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +

# Hint: to print more than one value on a line, you can print a 
# comma-separated sequence of values:




# By default, print advances to the next line, but you can 
# override that behavior and put a space at the end, like this:


# The output of these statements is '+ -'.

# A print statement with no argument ends the current line and 
# goes to the next line.



# (2) Write a function that draws a similar grid with four rows and four columns.
################################################################################
# Write your functions below:
# Body

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_row4():
    print ('+----+----+----+----+')

def print_column4():
    print ('|    |    |    |    |')

def print_columns4():
    do_four(print_column4)

def do_four_by_four():
    print_row4()
    print_columns4()

def print_four_by_four():
    do_twice(do_four_by_four)
    do_twice(do_four_by_four)
    print_row4()

def print_row2():
    print ('+----+----+')

def print_column2():
    print ('|    |    |')

def print_columns2():
    do_four(print_column2)

def do_two_by_two():
    print_row2()
    print_columns2()

def print_two_by_two():
    do_twice(do_two_by_two)
    print_row2()












# Write your functions above:
################################################################################
def main():
    print_four_by_four()
    print_two_by_two()
    print("Hello World!")
    



if __name__ == "__main__":
    main()