# Put your code here
intPrcNew = int(3)
intPrcOld = int(2)

intNew = input("Enter the number of new videos: ")
intOld = input("Enter the number of oldies: ")

totNew = float(intNew) * float(intPrcNew)
totOld = float(intOld) * float(intPrcOld)

intTot = float(totNew) + float(totOld)

print("The total cost is $" + str(intTot))
