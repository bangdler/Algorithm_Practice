
# a = [1, 2, 1, 4, 5]
#
# def solve(a):
#     return sum(a)

d_numbers = []
def dn(n):
    n_list = list(str(n))
    n_list = map(int, n_list)
    dn = n + sum(n_list)
    d_numbers.append(dn)

for i in range(1, 10001):
    dn(i)

answer = list(set(range(1, 10001)) - set(d_numbers))
answer.sort()
for a in answer:
    print(a)
# for a in answer:
#     print(a)
# for i in range(1, 10001):
#     if i in d_numbers:
#         pass
#     else:
#         print(i)

