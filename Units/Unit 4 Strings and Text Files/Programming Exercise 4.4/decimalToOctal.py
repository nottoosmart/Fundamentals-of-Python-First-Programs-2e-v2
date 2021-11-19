# Put your code here

decimal = int(input("Enter a decimal integer: "))
if decimal == 0: 
    print(0)
else:
    print("Quotient Remainder Octal")
    bstring = ""
    while decimal > 0:
        remainder = decimal % 8
        decimal = decimal // 8
        bstring = str(remainder) + bstring
        print("%5d%8d%12s" % (decimal, remainder, bstring))
    print("The binary representation is", bstring)  
# Put your code here
