
case_n = int(input())
uppers = []

for i in range(case_n):
    scores = list(map(int, input().split()))
    n = scores[0]
    scores = scores[1:]
    avg = sum(scores) / n
    count = 0
    for score in scores:
        if score > avg:
            count += 1
    upper_ratio = count / n * 100
    uppers.append(upper_ratio)

for i in range(case_n):
    print('%.3f' % round(uppers[i], 3), '%', sep='')
