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

def print_row():
    print ('+----+----+----+----+')

def print_column():
    print ('|    |    |    |    |')

def print_columns():
    do_four(print_column)

def do_grid():
    print_row()
    print_columns()

def print_grid():
    do_twice(do_grid)
    do_twice(do_grid)
    print_row()













# Write your functions above:
################################################################################
def main():
    print_grid()
    print("Hello World!")
    



if __name__ == "__main__":
    main()