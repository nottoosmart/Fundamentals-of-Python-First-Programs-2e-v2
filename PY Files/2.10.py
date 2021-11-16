# Put your code here
intWage = float(input("Enter the wage: $"))
intHours = int(input("Enter the regular hours: "))
intOvertime = int(input("Enter the overtime hours: "))

intReg = float(intWage) * int(intHours)
intOvr = int((1.5 * intWage) * intOvertime)

print("The total weekly pay is: $" + str(intReg + intOvr))
