import math

tolerance = 0.000001

# this is the Newton's function
def newton(x, estimate=1.0):
    estimate = (estimate + x / estimate) / 2
    difference = abs(x - estimate ** 2)
    if difference <= tolerance:
        return estimate
    else:
        return newton(x, estimate)


def limitReached(diff, tolerance):
  if (diff <= tolerance):
        val = True
    else:
        val = False
    return val

def improveEstimate(x, sqrtOfThis):
    return (sqrtOfThis + x / sqrtOfThis) / 2


def main():
    while True:
        x = input("Enter a positive number or enter/return to quit: ")
        if x == "":
            break
        x = float(x)
        sqrtOfThis = math.sqrt(x)
        improveEstimate(x, sqrtOfThis)
        print("\nThe program's estimate is", newton(x))
        print("Python's estimate is ", sqrtOfThis)


if __name__ == "__main__":
    main()
