
n = int(input())
score = list(map(int, input().split()))
max = max(score)

new_scores = []
for i in range(0, n):
    new_score = score[i] / max * 100
    new_scores.append(new_score)
new_aver = sum(new_scores) / n
print(new_aver)