# Put your code here
inputName = input("Enter the input file name: ")
outputName = input("Enter the output file name: ")

inputFile = open(inputName,'r')
outputFile = open(outputName, 'w')

for line in inputFile:
    outputFile.write(line)
inputFile.close()
outputFile.close()
