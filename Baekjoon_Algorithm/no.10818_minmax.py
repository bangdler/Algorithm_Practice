
n = int(input())
numbers = list(input().split())
a = min(map(int, numbers))
b = max(map(int, numbers))
print(a, b)