print('hello world')

x = 10
y = -20

a = x
b = y
x = b
y = a
print(x)
print(y)

def gap(*list):
    a = min(list)
    b = max(list)
    print(b, a)

gap(*(100, 200))
gap(10, 20, 30, 40)

ages = [19, 16, 24, 19, 23]
gap(*ages)

def conc(*a, **b):
    c = b.get('seperator')
    d = c.join(a)
    print(d)

conc('가난하다고해서', '해서', '외로움을', '모르겠는가', seperator='/')
conc(*'월화수목금토일', seperator='-')