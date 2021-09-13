num_stamp = 0

def stamp(num_stamp):
    num_stamp = num_stamp + 1
    print(num_stamp)
    return num_stamp


num_stamp = stamp(num_stamp)

def divide(number, by=2):
    print(number / by)


divide(7, 3)

def 동전계산(오백원=0, 백원=0, 오십원=0, 십원=0):
    return 오백원 * 500 + 백원 * 100 + 오십원 * 50 + 십원 * 10

def 음료선택(코코아=0, 커피=0):
    return 300 * 코코아 + 400 * 커피

def 주문():
    print("제품을 선택해주세요")
    a, b = map(int, input().split())
    result_1 = 음료선택(a, b)
    print("총금액은",result_1, "입니다.")
    print("동전을 넣어주세요")
    c, d, e, f = map(int, input().split())
    result_2 = 동전계산(c,d,e,f)
    print("투입금액은", result_2, "입니다.")
    print("거스름돈은", result_2 - result_1, "입니다.")

주문()