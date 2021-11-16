# Put your code here
f = open(input("Enter a filename: "), "r")
myDict = {}
linenum = 0

for line in f:
    line = line.strip()
    line = line.split()
    linenum += 1
    for word in line:
        word = word.strip()

        if not word in myDict:
            myDict[word] = []
        myDict[word].append(linenum)

for key in sorted(myDict):
    print(key, len(myDict[key]))
