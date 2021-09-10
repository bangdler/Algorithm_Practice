# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

i = 0
while i < 3:
    print('안녕')
    i += 1

rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
index = 0
while index < len(rainbow):
    print(rainbow[index])
    index += 1

# text = "아무 메시지나 입력하세요, 그만하려면 '그만'을 입력하세요."
# while text != '그만':
#     print('컴퓨터:', text)
#     text = input()

for color in rainbow:
    print(color)

def my_sum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

print(my_sum([1, 2, 3, 4, 5]))


total = 0
for n in range(2, 10000001, 2):
    total += n

print(total)

print('몇 번 반복하시겠습니까?')
n = int(input())
for _ in range(n):
    print('하이')

for i in range(4):
    print('현재반복주기 :', i)
    continue
    print('다음반복주기 :', i+1)

for i in range(4):
    print('현재반복주기 :', i)
    break
    print('다음반복주기 :', i+1)


total = 0
while True:
    print('더할 수를 입력하세요:', end='')
    user_input = input()
    if user_input == '그만':
        break
    if not user_input.isnumeric():
        print('잘못된 입력입니다.')
        continue

    total += int(user_input)
    print('합계:', total)

i = 0
while i < 3:
    print(i, '번ㅉㅐ 실행')
    i += 1
else:
    print('반복완료')


def first_even(numbers):
    """numbers에서 첫 번째 짝수를 찾아 화면에 출력한다."""
    '''numbers에서 첫 번째 짝수를 찾아 화면에 출력한다.'''
    for n in numbers:
        if n % 2 == 0:
            print(n, '이 첫 짝수입니다.')
            break
    else:
        print('짝수가 없습니다.')

first_even([1, 3, 5, 7, 55])
first_even([7, 5, 6, 4, 19, 91])


for i in range(2,10):
    for j in range(1,9):
        print(i * j, end=' ')
    print()
# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
