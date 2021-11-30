"""
File: CS_V11_CSLO_4.py
CS.V11.72781 Quiz - CSLO 4

1) Write a program in Python, C++, or C that gets an integer
from the user, prints out that value, then passes that value
to a function, that doubles the number and returns back out
the doubled number back to the main function and prints out
that value to the screen.

Hint: Use “Good Programming” practices such as comments,
descriptive variables and good-formatting output.

Grading Rubric:

1) Program complies/runs/produces the correct results: 60 Points

2) Well documented Program with comments: 20 Points

3) Other good programming styles such as indentation, descriptive variable
names and so on: 20 Points
"""


# doubleInput definition to double user's input.
def doubleInput(x):
    # Double user's number
    intDoubled = x * 2

    return intDoubled


def main():
    while True:
        # Get users number
        x = input("Enter a number or enter/return to quit: ")

        # Exit program if no value input
        if x == "":
            break

        # Convert user's input to a float value
        x = float(x)

        # Print user's input
        print("User's number is ", x)

        # Print user's number doubled
        print("User's number doubled is ", doubleInput(x))


if __name__ == "__main__":
    main()
