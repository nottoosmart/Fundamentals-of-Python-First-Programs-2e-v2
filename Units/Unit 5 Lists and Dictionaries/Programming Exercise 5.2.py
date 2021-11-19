# Put your code below:
#fileName = 'example.txt'
fileName = input("Enter the input file name: ")
f = open(fileName, 'r')

lines = []
count = ""

while True:

    line = f.readline()
    if line == "":
        break

    if count == "":
        count = 1
    else:
        count += 1

    lines.append(line)

print("The file has ", count, " lines.")

def main():
    while True:
        request = input("Enter a line number [0 to quit]: ")
        if request == "0":
            break
        else:
            item = int(request)-1
            if item >= count:
                print("ERROR: line number must be less than ", count)
                print("The file has ", count, " lines.")
            else:
                print(request," : ", lines[item])

if __name__ == "__main__":
    main()
