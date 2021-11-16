# Put your code here
bstring = input("Enter a string of octal digits: ")
decimal = 0
exponent = len(bstring) - 1
for digit in bstring:
    decimal = decimal + int(digit) * 8 ** exponent
    exponent = exponent - 1
print("The integer value is", decimal)
