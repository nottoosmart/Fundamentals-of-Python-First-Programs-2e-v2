# Put your code here
def decimalToRep(num,base1):
    base = ""
    while num > 0:
        one = int(num % base1)
        if one < 10:
            base += str(one)
        else:
            base += chr(ord('A')+one-10)
        num //= base1
    base = base[::-1]
    return base

# A main for testing your program
def main():
    print(decimalToRep(10, 10))
    print(decimalToRep(10, 8))
    print(decimalToRep(10, 2))
    print(decimalToRep(10, 16))

# The entry point for program execution
if __name__ == "__main__":
    main()
