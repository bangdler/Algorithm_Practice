print("today's coffee")
print('today\'s coffee')
print('today\'s coffee:\n"카페라테"\n"아메리카노"')
print('다음행으로 넘어갈 때는 개행문자(\\n)을 쓰세요')
print(r'다음행으로 넘어갈 때는 개행문자(\n)을 쓰세요')
print(r'today\'s coffee:\n"카페라떼"\n"아메리카노"')


a = """today's coffee:
"카페라떼"
"아메리카노" """

print(a.find('라'))
print(a.split('라'))
print(a.join('오주영'))
print(a.isalnum())
print(a.isalpha())
#
# order_memo = """주문1: 아메리카노
# 주문2: 카페라떼, 아메리카노"""
#
# print('주문수량:',order_memo.count('주문'))
# print('아메리카노:',order_memo.count('아메리카노'),'잔')

print(bool(0))
print(not(True and True or False))
print(bool(10 < 20 and 0))
print(type(False))

number = input()
a = int(a)
a = int(number)
print(a)
#
print(int(1.1))
#
# num_1 = int(input())
# num_2 = int(input())
# result = num_1 + num_2
# print('결과:', result)