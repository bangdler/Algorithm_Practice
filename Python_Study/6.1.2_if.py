print('hello monday')



#
# print('일요일 날씨를 말해주세요')
# 날씨 = input()
# if 날씨 == '비':
#     print('집에서 프로그램을 만들자')
# if 날씨 != '비':
#     print('나가서 운동을 하자')

# def absol():
#     a = int(input())
#     if a >= 0:
#         print(a)
#     if a < 0:
#         print(-a)
#
#
# absol()
#
# print('일요일 날씨를 말해주세요')
# 날씨 = input()
# if 날씨 == '비':
#     pass
# else:
#     print('공원에서 스케이트보드를 타자')
#
# print('일요일 날씨를 말해주세요')
# 날씨 = input()
# if not (날씨 == '비'):
#     print('공원에서 스케이트보드를 타자')


# print('일요일 낮의 기온을 입력해주세요요')
# 기온 = float(input())
# if 28.0 <= 기온:
#     print('바닷가에서 더위를 피하자')
# elif 16.0 <= 기온:
#     print('밖에서 데이트를 하자')
# elif 8.0 <= 기온:
#     print('카페에서 책을 읽자')
# else:
#     print('집에서 코딩이나 하자')

날씨, 요일 = input().split()
if (날씨 == '맑음') and (요일 == '일요일'):
    print('공원에서 스케이트보드를 타자')
else:
    print('퍼킹')

요일 = input()
가격 = 1000 if 요일 == '월요일' else 2500
print(가격)

