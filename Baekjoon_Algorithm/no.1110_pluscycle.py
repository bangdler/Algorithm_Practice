
n = int(input())
a = n
b = -1
i = 0
while b != n:
    a_1 = a // 10
    a_2 = a % 10
    a_s = a_1 + a_2
    b_1 = a_2
    b_2 = a_s % 10
    b = b_1 * 10 + b_2
    a = b
    i += 1
else:
    print(i)



