#[Built-in[Global scope[Enclosing scope[local scope]]]]  o Built-in --> Global scope --> Enclosing scope --> local scope
price = 100 # Global scope

def increment():
    price = 200 #Local scope
    result = price + 10
    print(result)
    return result

print(price)
price2 = increment()
print(price2)