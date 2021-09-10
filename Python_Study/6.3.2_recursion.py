
def 피보나치(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return 피보나치(n-1) + 피보나치(n-2)

for n in range(1, 12):
    print(피보나치(n), end=' ')