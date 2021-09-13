print('Hello juyoung~')

total = 0
i = 100
while i < 10000:
    total += i
    i += 5
print(total)

total = 0
for n in range(100, 10000, 5):
    total += n
print(total)


def max_list(list):
    max_val = 0
    for n in list:
        if n > max_val:
            max_val = n
    return max_val


print(max_list([3, 7, 3, 4, 5]))


def is_prime(a):
    n = 2
    if a == 1:
        return False
    while n < a:
        if a % n == 0:
            return False
        else:
            n += 1
    else:
        return True

print(is_prime(63))


total = 0
for n in range(1, 100, 1):
    if is_prime(n) == True:
        total += n
print(total)


##출력 안되는 경우##
False and print("참")
True or print("rj")