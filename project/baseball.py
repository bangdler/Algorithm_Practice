ans = input()

strike = 0
ball = 0
trial_n = 0

while trial_n < 10:
    strike = 0
    ball = 0
    trial = input()
    for i in range(len(trial)):
        if trial[i] == ans[i]:
            strike += 1
        else:
            if trial[i] in ans:
                ball += 1
    trial_n += 1
    print(trial_n, "of 10 trial", strike, "strike", ball, "ball")
    if strike == len(ans):
        print("Correct! answer =", ans)
else:
    print("You failed!")