def increment(x):
    return x + 1

result = 10
print(increment(result))

increment_v2 = lambda x: x + 1
print(increment_v2(20))

full_name = lambda name,last_name: f"Full name es {name.title()} {last_name.title()}"

text = full_name("jorge","lopez")
print(text)
