squares = []

for x in range(10):
    squares.append(x ** 2)

print(squares)
print(list(map(lambda a: a ** 2, range(10))))
print([x ** 2 for x in range(10)])


print(not'')
