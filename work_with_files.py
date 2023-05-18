import os

def quot_marks(file_path):
    if file_path[0] != '"' and file_path[0] != '\'' and file_path[-1] != '"' and file_path[-1] != '\'':
        file_path = ''.join(('"', file_path, '"'))
    return file_path

def manipulation(arg):
    while True:
        action = input("""Чтобы Вы хотели предпринять?
Выберите возможные действия с файлом:
W - полностью очистить данные файла и записать новые;
R - прочесть данные из файла;
A - дополнить существующие данные новыми данными;
D - удалить файл: 
Q - выйти из меню работы с файлом: """)
        if action == 'W':
            while True:
                confirmation = input("""Вы уверены, что хотите полностью очистить данные этого файла
и записать новые? Если да, введите Y; если нет, введите N: """)
                if confirmation != 'Y' and confirmation != 'N':
                    print("Ответ на распознан.")
                    continue
                elif confirmation == 'N':
                    break
                else:
                    with open(arg, 'w') as my_file:
                        print("Вводите информацию. Как только вся информация будет введена, введите quit")
                        while True:
                            text = input("Введите информацию: ")
                            if text != 'quit':
                                text += '\n'
                                my_file.write(text)
                            else:
                                break
                        break
        elif action == 'R':
            print("Начало документа")
            with open(arg, 'r') as my_file:
                for i in my_file:
                    print(i, end = "")
                print("Конец документа")
        elif action == 'A':
            with open(arg, 'a') as my_file:
                print("Вводите информацию. Как только вся информация будет введена, введите quit")
                while True:
                    text = input("Введите информацию: ")
                    if text != 'quit':
                        text += '\n'
                        my_file.write(text)
                    else:
                        break
        elif action == 'D':
            while True:
                confirmation = input("""Вы уверены, что хотите удалить этот файл?
Если да, введите Y; если нет, введите N: """)
                if confirmation != 'Y' and confirmation != 'N':
                    print("Ответ не распознан.")
                    continue
                elif confirmation == 'N':
                    break
                else:
                    os.remove(arg)
                    print("Файл удалён")
                    break
        elif action == 'Q':
            break

        else:
            print("Выбор не распознан.")
            continue

print("Привет!")

while True:
    start = input("""Добро пожаловать в главное меню.
Вы хотели бы создать новый файл или открыть существующий?
Введите new, если хотите создать новый файл, или ex, если хотите открыть существующий.
Введите rename, если хотите переименовать файл или директорию.
Введите quit, если хотите выйти из программы: """)
    if start == 'ex':
         while True:
            path = input("Введите, пожалуйста, путь к файлу: ")
            if os.path.exists(path) == False or os.path.exists(path) and path[-4:] != '.txt':
                print("Файл по этому пути не найден. Возможно, Вы ошиблись в написании.")
                while True:
                    command = input("""Хотите ввести путь еще раз?
Введите Y, если да, или N, если хотите вернуться в главное меню: """)
                    if command != 'Y' and command != 'N':
                        print("Ответ не распознан")
                        continue
                    else:
                        break
                    if command == 'Y':
                        break
                if command == 'N':
                    break
            else:
                print("Запрашиваемый файл найден")
                path = path.replace(os.sep, '/')
                manipulation(path)
                break
    elif start == 'new':
        while True:
            create_start = input("Хотите создать новую директорию? Введите Y, если да, или N, если нет: ")
            if create_start == 'Y':
                try:
                    create_dir = input("Введите путь к директории, которую Вы хотите создать, вместе с ее названием: ")
                    create_dir = create_dir.replace(os.sep, '/')
                    os.mkdir(create_dir)
                    print(f'Директория {os.path.basename(create_dir)} создана.')
                    pass
                except:
                    print("Что-то пошло не так. Возможно, директория уже существует, либо ввод осуществлен некорректно.")
                    continue
            elif create_start == 'N':
                pass
            else:
                print("Ответ не распознан")
                continue
            while True:
                try:
                    create_file = input("Введите путь к файлу, который Вы хотите создать, вместе с его названием: ")
                    create_file = create_file.replace(os.sep, '/')
                    if create_file[-4:] != '.txt':
                        create_file += ''.join('.txt')
                    new_file = open(create_file, 'x')
                    new_file.close()
                    print(f'Файл {os.path.basename(create_file)} создан.')
                    break
                except:
                    print("Что-то пошло не так. Возможно, файл уже существует, либо ввод осуществлен некорректно.")
                    continue
            break
        manipulation(create_file)
    elif start == "rename":
        try:
            current_name = input("Введите текущее имя файла или директории: ")
            new_name = input("Введите новое имя файла или директории: ")
            current_name = current_name.replace(os.sep, '/')
            new_name = new_name.replace(os.sep, '/')
            quot_marks(current_name)
            quot_marks(new_name)
            os.rename(current_name, new_name)
            print("Файл (директория) переименован(а)")
        except:
            print("""Что-то пошло не так. Возможно, ввод осуществлен некорректно.
Если файл не находится в текущей директории, необходимо прописать полный путь данного файла,
а также новое название файла, включая полный путь.""")
    elif start == 'quit':
        print("Благодарю за использование. До свидания!")
        break
    else:
        print("Выбор не распознан")
