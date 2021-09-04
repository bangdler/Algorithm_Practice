
def quadrant():
    a = int(input())
    b = int(input())
    if (a > 0) and (b > 0):
        return 1
    elif (a > 0) and (b < 0):
        return 4
    elif (a < 0) and (b > 0):
        return 2
    else:
        return 3


print(quadrant())

