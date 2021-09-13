print('hello world')

date = (1990, 11, 9)

def date_to(a, b, c):
    d = str(a) + '년' + str(b) + '월' + str(c) + '일'
    print(d)

date_to(date[0], date[1], date[2])
date_to(*date)
date_to(1993, *(6, 25))

def mean(*a):
    b = sum(a)
    c = len(a)
    print(b / c)


numbers = 1,2,3,4,5
mean(*numbers)

def cal(ratio, *list):
    a = (1 - ratio) * sum(list)
    print(a)

list = 100, 200, 300, 400, 200
cal(0.25, 100)
cal(0.25, *(100, 200, 300, 400, 200))
cal(0.25, *list)


def date_to(d, b, c):
    d = str(d) + '년' + str(b) + '월' + str(c) + '일'
    print(d)

date = {
    'd' : 1990,
    'b' : 11,
    'c' : 9}

date_to(**date)


def string(y, m, d, **kwargs):
    a = str(y) + '년' + str(m) + '월' + str(d) + '일' + str(kwargs.get('h')) + '시'
    print(a)


string(1993, 6, 25, h=12)

