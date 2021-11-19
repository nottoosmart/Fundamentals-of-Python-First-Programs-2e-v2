intIterations = int(input("Enter the number of iterations: "))

pi = 0

for i in range(intIterations):
    term = (-1) ** i /(2*i+1)
    pi = pi + term

pi = pi * 4

print("The approximation of pi is " + str(pi))
