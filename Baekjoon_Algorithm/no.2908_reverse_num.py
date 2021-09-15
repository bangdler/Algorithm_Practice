## 숫자를 거꾸로 읽고 비교한다.

a, b = input().split()
c = ''
d = ''

for i in range(2, -1, -1):
    c += a[i]
    d += b[i]

if int(c) > int(d):
    print(c)
else:
    print(d)

