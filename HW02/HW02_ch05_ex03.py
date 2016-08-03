#!/usr/bin/env python
# HW02_ch05_ex03

# If you are given three sticks, you may or may not be able to arrange them in a 
# triangle. For example, if one of the sticks is 12 inches long and the other 
# two are one inch long, it is clear that you will not be able to get the short 
# sticks to meet in the middle. For any three lengths, there is a simple test to
# see if it is possible to form a triangle:

#   If any of the three lengths is greater than the sum of the other two, then 
#   you cannot form a triangle. Otherwise, you can. (If the sum of two lengths
#   equals the third, they form what is called a "degenerate" triangle.)

# (1) Write a function named is_triangle that takes three integers as arguments, 
# and that prints either "Yes" or "No," depending on whether you can or cannot 
# form a triangle from sticks with the given lengths.

# (2) Write a function that prompts the user to input three stick lengths, 
# converts them to integers, and uses is_triangle to check whether sticks with 
# the given lengths can form a triangle.

################################################################################
# Write your functions below:
# Body
def is_triangle(s1,s2,s3):
    if (s1 + s2 < s3) or (s2 + s3 < s1) or (s1 + s3 < s2):
        print ('No')
    else:
        print ('Yes')

def check_stick_lengths():
    s1 = input('Input value for side 1\n')
    s2 = input('Input value for side 2\n')
    s3 = input('Input value for side 3\n')
    is_triangle(int(s1), int(s2), int(s3))






# Write your functions above:
################################################################################
def main():
    is_triangle(1,2,3)
    is_triangle(1,2,4)
    is_triangle(1,5,3)
    is_triangle(6,2,3)
    #and a function call for
    check_stick_lengths()
    print("Hello World!")



if __name__ == "__main__":
    main()