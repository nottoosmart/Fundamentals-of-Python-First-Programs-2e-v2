# Put your code here:
from math import exp
side_a = int(input("Enter the first side: "))
side_b = int(input("Enter the second side: "))
side_c = int(input("Enter the third side: "))

side_a_len = int(side_a * side_a)
side_b_len = int(side_b * side_b)
side_c_len = int(side_c * side_c)

intTot = int(side_a_len + side_b_len + side_c_len)
list = [side_a_len, side_b_len, side_c_len]
intLargest = max(list)

if int(intTot - intLargest) == int(intLargest):
    print("\nThe triangle is a right triangle")
else:
    print ("\nThe triangle is not a right triangle")
