# Put code here
import math

fltRadius = float(input("Radius = "))
fltDiameter = float(fltRadius * 2)

print("\nDiameter      : " + str(fltDiameter))
print("Circumferemce : " + str(fltDiameter * math.pi))
print("Surface area  : " + str(4 * math.pi * math.pow(fltRadius,2)))
print("Volume        : " + str(4/3 * math.pi * math.pow(fltRadius,3)))
