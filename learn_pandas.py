import pandas as pd
from matplotlib import pyplot as plt, style
# cbr.ru/development/sxml
# https://cbr.ru/scripts/XML_val.asp?d=0

while True:
    currency = int(input("Какая валюта Вас интересует? Введите 0, если доллар; 1, если евро; 2, если юань (за 10 июяней): "))
    if currency == 0:
        currency = 'R01235'
        break
    elif currency == 1:
        currency = 'R01239'
        break
    elif currency == 2:
        currency = 'R01375'
        break
    else:
        print("Код валюты введен неверно. Попробуйте еще раз")

date_start = input("С какого числа интересует курс? ")
date_fin = input("По какое число интересует курс? ")
url = 'http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={}&date_req2={}&VAL_NM_RQ={}'.format(date_start, date_fin, currency)

# url = 'http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1={}&date_req2={}&VAL_NM_RQ=R01239'.format(date_start,date_fin)
# print(url)
#url = 'http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1=26.01.2023&date_req2=01.02.2023&VAL_NM_RQ=R01239'
a = pd.read_xml(url)
print(a)
print(type(a))
mas = []
for i in range(0,len(a)):
    mas.append([a.iloc[i].iloc[0], a.iloc[i].iloc[3]])
print(mas)

# # rate = '76,3884'
# # print(float(rate.replace(',', '.')))
#
x,y = [], []
for i in range(0, len(mas)):
    x.append(mas[i][0])
    y.append(float(mas[i][1].replace(',', '.')))
print(x)
print(y)


plt.plot(x,y)
plt.xlabel("Дата")
plt.ylabel("Курс евро")
plt.title("Котировки евро за последнее время")
# Повернуть ось, чтобы данные не наезжали друг на друга в графике. 45 здесь - угол поворота
plt.xticks(rotation=45)
plt.show()



