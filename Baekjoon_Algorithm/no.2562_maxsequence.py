
numbers = []
for i in range(0, 9):
    a = int(input())
    numbers.append(a)
max = max(numbers)
seq = numbers.index(max) + 1
print(max)
print(seq)