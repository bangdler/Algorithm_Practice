
n = int(input())
for i in range(1, n+1):
    star = str("*" * i)
    print(star.rjust(n))

n = int(input())
for i in range(1, n+1):
    space = str()
    star = str("*" * i)
    print('{0:>{1}}'.format(star, n))
