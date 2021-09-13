drink_dict = {
    '아메리카노' : 2500,
    '카페라테' : 3000,
    '딸기 주스' : 3000,
}

drink_dict['콜라'] = 1500
drink_dict['아메리카노'] = 2600
del drink_dict['콜라']

print(drink_dict)
print('cat' in drink_dict)
print(drink_dict['아메리카노'])

price_list = [2500, 3000, 3000]
drink_list = ['아메리카노', '카페라테', '딸기 주스']
menu_dict = dict(zip(drink_list, price_list))
print(menu_dict)
print(menu_dict.values())
print(menu_dict.keys())

food_kcal = {
    '밀가루' : 364,
    '피망' : 20.1,
    '올리브' : 115,
    '돼지고기' : 242.1,
}

def cal(a, b):
    c = food_kcal[a] * b / 100
    print(c)

cal('돼지고기', 500)

food_kcal['치즈'] = 402.5

cal('치즈', 500)