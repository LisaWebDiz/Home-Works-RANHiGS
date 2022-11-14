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