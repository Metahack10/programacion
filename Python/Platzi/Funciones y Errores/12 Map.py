numbers = [1, 2, 3, 4]
numbers_v2 = []

for i in numbers:
    numbers_v2.append(i * 2)

print(numbers)
print(numbers_v2)

numbers_v3 = list(map(lambda i: i * 2, numbers))
print(numbers_v3)

numbers2 = [5, 6, 7]

print(numbers)
print(numbers2)
result = list(map(lambda x, y: x + y, numbers, numbers2))
print(result)
