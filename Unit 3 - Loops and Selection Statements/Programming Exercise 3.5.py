# initial number of organisms
intOrg = int(input("Enter the initial number of organisms: "))

# rate of growth
growthRate = float(input("Enter the rate of growth [a real number > 1]: "))

# number of hours it takes to achieve rate
hrsAchRate = int(input("Enter the number of hours to achieve the rate of growth: "))

# number of hours the pop. grows
totHrs = int(input("Enter the total hours of growth: "))

loopNum = totHrs // hrsAchRate

# Not needed (Keeping it simple)
# totPop = intOrg * growthRate

for number in range(0, loopNum):
    # Replaced with code below to simplify and correct math
    # totPop = totPop * number

    intOrg = intOrg * growthRate


print("The total population is", intOrg)
