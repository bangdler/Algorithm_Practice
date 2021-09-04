
def alarm_early():
    a, b = map(int, input().split())
    if b >= 45:
        alarm_min = b - 45
        alarm_hrs = a
    elif b < 45:
        alarm_min = 60 - (45 - b)
        if a == 0:
            alarm_hrs = 23
        else:
            alarm_hrs = a - 1
    print(alarm_hrs, alarm_min)

alarm_early()

a, b = map(int, input().split())
if b >= 45:
    b = b - 45
    a = a
elif b < 45:
    b = 60 - (45 - b)
    if a == 0:
        a = 23
    else:
        a = a - 1
print(a, b)