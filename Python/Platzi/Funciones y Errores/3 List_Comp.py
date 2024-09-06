#! [element for element in iterable] 
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
#! Matrices
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(matrix)
print(transposed)
print(matrix[0])
print(matrix[2][1])
