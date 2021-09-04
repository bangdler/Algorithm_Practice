
n, x = map(int, input().split())
numbers = list(input().split())
# answer = []
# for i in range(0, n):
#     if x > int(numbers[i]):
#         answer.append(numbers[i])
#


for number in numbers:
    if x > int(number):
        print(number, end=" ")