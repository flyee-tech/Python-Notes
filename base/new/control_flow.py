# if Statements
# x = int(input("Please inter an Integer: "))
# if x < 0:
#     x = 0
#     print("Negative changed to zero!")
# elif x == 0:
#     print("Zero")
# elif x == 1:
#     print("Single")
# elif x > 1:
#     print("More")

# for Statements
words = ['one', 'two', 'three', 'four']
for word in words[:]:
    print(word, len(word))

# The range function
r1 = range(5)
r2 = range(5, 10)
r3 = range(1, 100, 10)  # 每10次生成从1到100的list
r4 = range(-10, -100, -2)

for r in r4:
    print(r, end=" ")
print()

# break and continue Statements, and else Clauses on Loops
for n in range(2, 10):  # 素数or质数的查找
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
            break
    else:
        print(n, 'is a prime number!')

# pass Statements
while True:
    pass
