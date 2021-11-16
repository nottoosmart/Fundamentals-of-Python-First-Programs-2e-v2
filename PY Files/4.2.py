# Put your code here
code = input("Enter the coded text: ")
distance = int(input("Enter the distance value: "))
plainText = ''
for ch in code:
    ordValue = ord(ch)
    cipherValue = ordValue - distance
#    if cipherValue < ord('a'):
#        cipherValue = ord('z') - \
#                        (distance - (ord('a') - ordValue - 2))
    plainText += chr(cipherValue)
print(plainText)
