print('Стоимость 1кг черешни - 34 руб.')
weight = input('Введите вес покупаемой черешни: ')
money = input('Введите количество денег: ')
print("Было передано", money, 'руб.')
print('Сдача составляет:', float(money)-float(weight)*34)
