## 단어 중 가장 많은 알파벳 세기 (대소문자 구분 없이)

word = input()

results = [0 for _ in range(26)]

WORD = word.upper()
for i in WORD:
    alpha_n = ord(i) - 65
    results[alpha_n] += 1

max_alphabet = max(results)
if results.count(max_alphabet) >= 2:
    print("?")
else:
    a = results.index(max_alphabet) + 65
    answer = chr(a)
    print(answer)
