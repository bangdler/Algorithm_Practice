a, b = map(int, input('두개의 숫자를 입력하세요:').split())

a = (1-2j).real
b = (1-2j).imag

print (a, b)

a = 0x7d0
b = 2021-0o22+1
c = 2021-18
print(a, b, c)

a = -25287e-2
print(a)

def almost_equal():
    a, b = map(float, input().split())
    print(-0.0001 < (a-b) < 0.0001)


almost_equal()
