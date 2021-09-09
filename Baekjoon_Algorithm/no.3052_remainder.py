
remainders = set()
for i in range(0, 10):
    a = int(input())
    b = a % 42
    remainders.add(b)

n = len(remainders)
print(n)