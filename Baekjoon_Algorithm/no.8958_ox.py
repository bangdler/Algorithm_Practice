
n = int(input())
scores = []

for i in range(0, n):
    ox = list(input())
    score = 0
    for j in range(0, len(ox)):
        if j != 0 and (ox[j] == 'O') and (ox[j - 1] == 'O'):
            continue
        elif ox[j] == 'O':
            k = 0
            while j + k < len(ox) and ox[j + k] == 'O':
                score += k + 1
                k += 1
    scores.append(score)

for i in range(0, n):
    print(scores[i])

#
#
# n = int(input())
# total = []
#
# for i in range(n):
#     scores = []
#     ox = list(input())
#     score = 0
#     for answer in ox:
#         if answer == 'O':
#             score += 1
#         else:
#             score = 0
#         scores.append(score)
#     a = sum(scores)
#     total.append(a)
#
# for i in range(0, n):
#     print(total[i])
#
# # a = 'OOXXOXXOOOO'
# # print('O' * 3)
# # print(a.count('O' * 4))
# # print(a.count('O' * 3))
# # print(a.count('O' * 2))
# # print(a.count('O'))