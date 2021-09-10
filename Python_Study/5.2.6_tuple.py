a = [1, 2]
b = (1, 2)

print(a==b)

days = '일', '월', '화', '수'
print(days[::-1])
print(days[::2])

days = days + ('목', '금', '토')
print(days[2::3])
print(days.extend(('목', '금', '토')))