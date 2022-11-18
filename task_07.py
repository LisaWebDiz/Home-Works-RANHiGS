titles = {
    'Кроссовки тип 3 - Adidas': '100000110',
    'Мячик тип 2 - Adidas': '100000146',
    'Кепка тип 1 - Adidas': '100000149',
    'Ремень тип 2 - Nike': '100000194',
    'Футболка тип 1 - Adidas': '100000224',
    'Шапка тип 5 - Puma': '100000280',
}

sales = {
    '100000110': [{'quantity': 31, 'price': 1637}],
    '100000146': [ {'quantity': 4, 'price': 45}, {'quantity': 10, 'price': 48}],
    '100000149': [ {'quantity': 28, 'price': 279}, {'quantity': 32, 'price': 291}],
    '100000194': [{'quantity': 8, 'price': 220}, {'quantity': 1, 'price': 170}],
    '100000224': [{'quantity': 61, 'price': 438}, {'quantity': 23, 'price': 302},  {'quantity': 50, 'price': 412}],
    '100000280': [{'quantity': 26, 'price': 175}, ]
}

# Создание переменной кода товара:
for good_name in titles:
  good_code = titles[good_name]
# Инициация переменных для подсчета количества и стоимости товаров:
  total_quantity = 0
  total_price = 0
# Получение списка на складе по коду товара:
# Подсчет количества товара
# Подсчет стоимости товара
  for tuple in sales[good_code]:
    total_quantity = total_quantity + tuple['quantity']
    
    total_price = total_price  + tuple['quantity'] * tuple['price']
# вывод на консоль количества и стоимости товара на складе     
  print(f'{good_name} - {total_quantity} шт., общей стоимостью {total_price} рублей.')
    
# Отлично!
