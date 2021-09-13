
# a_list = range(10)   # ㄴㄴ
# a_list = [range(10)] # ㄴㄴ
# a_list = list(range(10))
# print(a_list)
#

b_list = list(range(0, 20, 2))
print(b_list)

경 = 10000
print(list(range(0, 경, 2))[-2])

print(list(range(0, 100, 2))[2])
a = list(range(0, 80, 4))
b = list(range(0, 80, 4))[1:10:3]
print(a)
print(b)

c = list(tuple('일월화수목금토'))
print(c)

print(''.join(['가난하다고','외로움을','모르겠느냐']))
print(''.join(('가난하다고','외로움을','모르겠느냐')))
print(' '.join(['가난하다고','외로움을','모르겠느냐']))

m_8_list = list(range(0, 100, 8))
print(m_8_list)