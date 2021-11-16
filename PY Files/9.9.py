# Put your code here
def isSorted(lyst):
    listTest = lyst[:]
    listTest.sort()
    if (listTest == lyst):
        flag = 1
    else :
        flag = 0

    if (flag == 1):
        return (True)
    else:
        return (False)


# A main for testing your code
def main():
    lyst = []
    print(isSorted(lyst))
    lyst = [1]
    print(isSorted(lyst))
    lyst = list(range(10))
    print(isSorted(lyst))
    lyst[9] = 3
    print(isSorted(lyst))

if __name__ == "__main__":
    main()
