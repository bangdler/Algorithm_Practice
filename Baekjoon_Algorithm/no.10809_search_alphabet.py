
s = input()
alphabet = []
answer = []
for i in range(97, 123):
    alphabet.append(chr(i))
## alphabet a~z 까지 속해있는지 확인한다.
for i in alphabet:
    position = s.find(i)
    print(position, end=' ')



