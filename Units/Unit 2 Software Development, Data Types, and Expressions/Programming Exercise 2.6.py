# Modify the following code
import math

# Request the input
mass = float(input("Enter the object's mass: "))
velocity = float(input("Enter the object's velocity: "))

# Compute the results
momentum = mass * velocity

# Display the results

print ("\nMass: " + str(int(mass)))
print ("Velocity: " + str(velocity))
print ("\nThe object's momentum is " + str(momentum))
print ("The object's kinetic energy is " + str(1/2 * mass * math.pow(velocity,2)))
