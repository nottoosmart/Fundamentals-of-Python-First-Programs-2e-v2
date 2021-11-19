# Put your code here
import math

intSmall = int(input("Enter the smaller number: "))
intLarge = int(input("Enter the larger number: "))

intGCD = math.gcd(intSmall,intLarge)

print("\nThe greatest common divisor is "+ str(intGCD))
