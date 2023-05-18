print("Добро пожаловать в калькулятор!")
while True:
    action = input("""Для сложения введите команду +
для вычитания введите команду -
для умножения введите команду *
для деления введите команду /
для целочисленного деления введите команду //
для возведения в степень введите команду **
для нахождения остатка от деления введите команду %
для выхода из калькулятора введите stop
Введите команду: """)
    if action == "+" or action == "-" or action == "*" or action == "/" or action == "//" or action == "**" or action == "%":
        while True:
            try:
                first_num = float(input("Введите первое число: "))
                break
            except ValueError:
                print('Первое число введено некорректно. Попробуйте еще раз')
        while True:
            try:
                second_num = float(input("Введите второе число: "))
                if action == "/":
                    try:
                        print(f'Результат деления {first_num} на {second_num} =', first_num / second_num)
                        break
                    except ZeroDivisionError:
                        print("На ноль делить нельзя")
                elif action == "//":
                    try:
                        print(f'Результат целочисленного деления {first_num} на {second_num} =', first_num // second_num)
                        break
                    except ZeroDivisionError:
                        print("На ноль делить нельзя")
                elif action == "%":
                    try:
                        print(f'Результат остатка от деления {first_num} на {second_num} =', first_num % second_num)
                        break
                    except ZeroDivisionError:
                        print("На ноль делить нельзя")
                else:
                    break
            except ValueError:
                print("Второе число введено некорректно. Попробуйте еще раз")
        if action == "+":
            print(f'Результат сложения {first_num} и {second_num} =', first_num + second_num)
        elif action == "-":
            print(f'Результат вычитания {second_num} из {first_num} =', first_num - second_num)
        elif action == "*":
            print(f'Результат умножения {first_num} на {second_num} =', first_num * second_num)
        elif action == "**":
            print(f'Результат возведения в степень {first_num} в {second_num} =', first_num ** second_num)
    elif action == "stop":
        print("Благодарю за использование. До свидания!")
        break
    else:
        print("Команда введена некорректно. Попробуйте еще раз")
