def median(numbers):
    numbers.sort()
    midIndex = len(numbers) // 2

    if len(numbers) % 2 == 1:
        return numbers[midIndex]
    else:
        return (numbers[midIndex] + numbers[midIndex - 1]) / 2

def mean(numbers):
    total = 0

    for number in numbers:
        total += number

    return total / len(numbers)


def mode(numbers):
    result = numbers[0]
    count = 0

    for num in numbers:
        if numbers.count(num) >= count:
            count = numbers.count(num)
            result = num

    return result

def main():

    userList = [3, 1, 7, 1, 4, 10]

    print("List:", userList)
    print("Mode:", mode(userList))
    print("Median:", median(userList))
    print("Mean:", mean(userList))


main()
