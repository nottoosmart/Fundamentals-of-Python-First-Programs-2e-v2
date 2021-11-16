# Put your code here:
intHeight = int(input('Enter the height from which the ball is dropped: '))
intIndex = float(input('Enter the bounciness index of the ball: '))
intBounces = int(input('Enter the number of times the ball is allowed to continue bouncing: '))

intdist = 0

for eachBounce in range(1,intBounces+1):
    intrebound = intHeight * intIndex
    intdist += intrebound + intHeight
    intHeight = intrebound

print("Total distance traveled is: " + str(float(intdist)) + " units.")
