
a = int(input())
b = int(input())
c = int(input())

d = a * b * c
numbers = list(str(d))
for i in range(0, 10):
    n = numbers.count(str(i))
    print(n)
