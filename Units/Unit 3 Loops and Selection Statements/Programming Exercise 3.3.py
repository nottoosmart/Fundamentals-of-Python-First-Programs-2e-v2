import math
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
count = 0
maxGuesses = round(math.log(larger - smaller + 1, 2))
while True:
    count += 1
    print(smaller, larger)
    yourNumber = (smaller + larger) // 2
    print("Your number is", yourNumber)
    answer = input("Enter =, <, or >: ")
    if answer == "=":
        print("Hooray, I've got it in", count, "tries!")
        break
    elif count == maxGuesses:
        print("I'm out of guesses, and you cheated!")
        break
    elif answer == "<":
        larger = yourNumber - 1
    else:
        smaller = yourNumber + 1
