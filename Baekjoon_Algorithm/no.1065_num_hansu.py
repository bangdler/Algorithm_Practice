hansu = []

def hansu_find(n):
    differences = set()

    if len(n) < 3:
        hansu.append(n)
    else:
        for i in range(len(n) - 1):
            diff = int(n[i]) - int(n[i + 1])
            differences.add(diff)
        if len(differences) == 1:
            hansu.append(n)

num = input()
for i in range(1, int(num)+1):
    hansu_find(str(i))
print(hansu)
print(len(hansu))







