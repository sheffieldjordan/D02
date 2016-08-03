#!/usr/bin/env python
# HW02_ch05_ex00 (See 5.9)

# Write a function called do_n that takes a function object and a number, n, as 
# arguments, and that calls the given function n times.

################################################################################
# Write your functions below:
# Body

def do_n(fn,x):
	if x <= 0: #If x is less than or equal to 0
		return #then the operation ends
	fn() #Execute the argument-function-object if the 'if' condition is not met.
	do_n(fn, x-1) #Execute the the do_n function again, but decrease the counter, n, by 1. 







# Write your functions above:
def print_hello():
    print("Hello World")
################################################################################
def main():
    do_n(print_hello, 10) #Prints Hello World 10 times, then stops. 
    



if __name__ == "__main__":
    main()