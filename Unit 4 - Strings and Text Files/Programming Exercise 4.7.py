"""
def binary_string(num):
    bit_string = "{0:b}".format(num);
    return bit_string
"""

def string_binary(num):
    string_bit = int(num, 2)
    string_bit = string_bit - 1

    ascii_character = chr(string_bit)
    return ascii_character

stringText = input("Enter a string: ")

bit_list = []

splitText = stringText.split()

for textValues in splitText:
    strChr = textValues[-1:]+textValues[0:-1]
    strChrCon = string_binary(strChr)
    bit_list.append(strChrCon)

output = ""

for bit in bit_list:
    output += bit
print(output)
