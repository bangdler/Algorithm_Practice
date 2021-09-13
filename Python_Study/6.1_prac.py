print('hello world~')


def price():
    quan = int(input())
    if 10 > quan:
        price = 100
    elif 10 <= quan < 30:
        price = 95
    elif 30 <= quan < 100:
        price = 90
    else:
        price = 85
    total = quan * price
    print(total)


price()


def is_leap(year):
    if year % 400 == 0:
        leap = 'true'
    elif year % 100 == 0:
        leap = 'false'
    elif year % 4 == 0:
        leap = 'true'
    else:
        leap = 'false'
    return leap


def days():
    year, month = map(int, input().split(','))
    t_one = [1, 3, 5, 7, 8, 10, 12]
    if (is_leap(year) == 'true') and (month == 2):
        day = 29
    elif (is_leap(year) == 'false') and (month == 2):
        day = 28
    elif month in t_one:
        day = 31
    else:
        day = 30
    return day


print(days())


odd = [1, 3, 5, 7, 9]
number = int(input())
if number in odd:
    print('true')
else:
    print('false')


def bmi(w, t):
    bmi = w / (t * t)
    return condition(bmi)


def condition(bmi):
    if 18.5 > bmi:
        c = '저체중'
    elif 18.5 <= bmi < 23:
        c = '정상'
    elif 23 <= bmi < 25:
        c = '과체중'
    else:
        c = '비만'
    return c


print('키를 입력하세요(m):', end='')
t = float(input())
print('몸무게를 입력하세요(kg):', end='')
w = float(input())
print(bmi(w, t), '입니다.')


def ab_num():
    a = float(input())
    a = a if a >= 0 else -a
    return a


print(ab_num())