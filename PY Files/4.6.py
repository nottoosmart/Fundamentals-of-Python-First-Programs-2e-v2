def binary_string(num):
    bit_string = "{0:b}".format(num);
    return bit_string

strInput = input("Enter a string: ")

ltrList = []

for ltr in strInput:
    ltrASCII = ord(ltr)

    ltrNext = int(ltrASCII) + 1

    binaryCode = binary_string(ltrNext)

    codeRearrange = binaryCode[1:]+binaryCode[0]

    ltrList.append(codeRearrange)

output = ""

for ltrCode in ltrList:
    output += ltrCode + " "

print(output)
