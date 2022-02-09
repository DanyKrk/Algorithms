# sortowanie bombelkowe

numbers = [10, 4, 19, 6, 20, 21, 22, 5]

n = len(numbers)

for j in range(n-1):
    for i in range(n - 1):
        if numbers[i] > numbers[i + 1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]

for x in numbers:
    print(x)
