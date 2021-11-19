# Put your code here

intStart = input("Enter the starting salary: $")

intIncrease = input("Enter the annual % increase: ")
intPercent = int(intIncrease) / 100

intYears = input("Enter the number of years: ")

count = 0

# Display the header for the table
print("%4s%9s" % ("Year", "Salary"))

print("%12s" % ("-------------"))

for eachYear in range(0, int(intYears)):
    count += 1
    if count == 1:
        print("%4d%9.2f" % (count, float(intStart)))
    else:
        intInc = float(intStart) * float(intPercent)
        intStart = float(intStart) + float(intInc)
        print("%4d%9.2f" % (count, float(intStart)))
