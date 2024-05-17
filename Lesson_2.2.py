cost = input('Цена товара: ')
weight = input('Вес товара: ')
money = input('Количество денег у покупателя: ')
print('Сдача составляет:', int(float(money)-float(weight)*float(cost)))
