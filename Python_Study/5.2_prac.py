print('hi')

def center(a):
    b = len(a)
    c = b // 2
    print(a[c])


center(['가', '나', '다', '라', 7, 9, 10])

def mirror(a):
    b = a[::-1]
    a.pop()
    print(a + b)


mirror([1, 2, 3])

def minmax(a):
    print([min(a), max(a)])

minmax((100, 200))
minmax([92, -21, 0, 104, 51, 76, -92])
minmax(['파','이','썬','프','로','그','래','밍'])


def mean(a):
    b = len(a)
    c = sum(a) / b
    print(c)

mean([92, -21, 0, 104, 51, 76, -92])

stations = []
stations.append('서울')
stations += (['수원', '대전'])
stations.extend(['밀양', '부산'])
stations.insert(3, '동대구')

print(stations)
print(stations.pop())
print(stations.remove('수원'))
print(stations)


a = range(0, 10, 2)
b = list(a)
print(b)
print(sum(b))

a = range(10)[::-1]
b = list(a)
print(b)

def reverse(a):
    b = a[::-1]
    print(b)

reverse([10, 20, 30, 40])
reverse(tuple('일월화수목금토'))
reverse(range(10))
reverse('파이썬 프로그래밍')
