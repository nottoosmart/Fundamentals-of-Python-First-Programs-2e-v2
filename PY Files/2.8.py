# Put your code here
import math
intSeconds = int(365 * 24 * math.pow(60,2))
intRate = int(3 * math.pow(10,8))
intDistance = int(intSeconds * intRate)


#print("seconds in year " + str(intSeconds))

#print("meters per second is " + str(intRate))

print("Light travels " + str(intDistance) + " meters in a year.")
