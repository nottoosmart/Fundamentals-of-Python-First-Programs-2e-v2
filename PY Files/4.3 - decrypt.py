inputName = input("Enter the input file name: ")
outputName = input("Enter the output file name: ")
distance = int(input("Enter the distance value: "))

inputFile = open(inputName, 'r')
outputFile = open(outputName, 'w')

code = ""

for line in inputFile:
    for ch in line:
        ordValue = ord(ch)
        cipherValue = ordValue - distance
        if cipherValue > ord('z'):
            cipherValue = ord('a') + distance - \
                        (ord('z') - ordValue + 1)
        code += chr(cipherValue)

outputFile.write(code)

inputFile.close()
outputFile.close()
