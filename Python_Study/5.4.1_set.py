print('hello world')

even = set(range(0, 10000, 2))
odd = set(range(1, 10000, 2))

wild = {'사자', '박쥐', '늑대', '곰'}
wing = {'독수리', '매', '박쥐'}
sea = {'참치', '상어', '문어 괴물'}

animal = wild.union(wing)
print(animal)
print(wild | wing | {'human'})

print(wild.intersection(wing))
print(wild.intersection(sea))

print(wild ^ wing)
print(wild <= animal)
print(len(wild))

week = {'월', '화', '수', '목', '금', '토', '일'}
working = {'월', '화', '수', '목', '금'}
holi = {'토', '일'}

def is_working(a):
    print (a in holi)

is_working('월')

a = set(range(0, 1000, 3))
b = set(range(0, 1000, 4))
c = a.union(b)
print(len(c))

d = a.intersection(b)
print(len(d))

e = a.difference(b)
print(len(e))