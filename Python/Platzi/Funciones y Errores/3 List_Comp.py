#[element for element in iterable]
numbers = []
for element in range(1,11):
    numbers.append(element * 2)

print(numbers)

numbers_v2 = [element * 2 for element in range(1,11)]
print(numbers_v2)

#[element for element in iterable if condition]
par = []
for element in range(1,11):
    if element %2 ==0:
        par.append(element * 2)
print(par)

par_v2 = [element * 2 for element in range(1,11) if element % 2 ==0]
print(par_v2)
