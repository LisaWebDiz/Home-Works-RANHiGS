# Зарплата сотрудника составляет salary руб., 
# Расходы на проживание превышают зарплату и составляют expenses руб. в месяц. 
salary, expenses = 10000, 12000
months = 12
year_sum = expenses
# Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
for i in range(2, months+1):
  expenses = expenses * 1.03
  year_sum += expenses
# Расчет суммы денег, которую необходимо взять в долг, чтобы можно было прожить ближайший год 
  money_needed = round(year_sum - salary * months, 2)
print(f'Необходимо взять в долг {money_needed} рублей')

# Отлично. Можно еще через while
# Решение 1
i = 0
months_expenses = 0
money_needs = 0

while i < 12:

    if i == 0:
        months_expenses = expenses
    elif i >= 1:
        months_expenses *= 1.03
    i += 1
    difference = round(months_expenses-salary, 2)
    money_needs += difference
    print('Расходы в', i, 'месяце:', difference, ', Итого за', i, 'мес.:', round(money_needs,2))

print('Сотруднику необходимо взять', round(money_needs,2), 'рублей')
