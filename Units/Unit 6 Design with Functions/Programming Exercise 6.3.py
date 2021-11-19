# Modify the code below
"""
File: newton.py
Project 6.2
Compute the square root of a number (uses recursive function).
1. The input is a number, or enter/return to halt the
   input process.
2. The outputs are the program's estimate of the square root
   using Newton's method of successive approximations, and
   Python's own estimate using math.sqrt.
"""

import math


TOLERANCE = 0.000001


def newton(x, estimate = 1.0):
    """Returns the square root of x."""

    difference = abs(x - estimate ** 2)
    if difference <= TOLERANCE:
        return estimate
    else:
        return newton(x, (estimate + x / estimate) / 2)

def main():
    while True:
        x = input("Enter a positive number or enter/return to quit: ")
        if x == "":
             break
        x = float(x)

        print("The program's estimate is", newton(x, 1))
        print("Python's estimate is     ", math.sqrt(x))

if __name__ == "__main__":
    main()
