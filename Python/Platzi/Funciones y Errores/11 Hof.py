def increment(x):
    return x + 1

def high_over_func(x, func):
    return x + func(x)

result = high_over_func(2,increment)
print(result)

incre = lambda x: x + 1
hof = lambda x, func: x + func(x)

result = hof(2,incre)
print(result)
result = hof(2, lambda x: x * 5)
print(result)
