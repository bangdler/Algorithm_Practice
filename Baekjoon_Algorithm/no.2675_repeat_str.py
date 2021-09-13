## 반복할 문자열 case 입력 후 반복할 횟수와 문자를 넣는다.
## 1시간 소요

n = int(input())
answer = []
for i in range(n):
    r = list(map(str, input().split()))
    str_ = r[1]
    repeat = int(r[0])
    str_0 = ""
    for i in range(len(str_)):
        str_repeat = ""
        str_repeat = str_[i] * repeat
        str_0 = str_0 + str_repeat
    answer.append(str_0)

for i in answer:
    print(i)

