from config import tg_bot_token

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import random

bot = Bot(token = tg_bot_token)
dp = Dispatcher(bot)

HELP = """
/help - вывести список доступных команд
/add - добавить задачу в список
/show - напечатать все добавленные задачи"""

tasks = {
    }

def add_todo (date, task):
  if date in tasks:
      tasks[date].append(task)
  else:
      tasks[date] = [task]

@dp.message_handler(commands = ["start"])
async def start_command(message: types.Message):
    await message.answer("Привет!")

@dp.message_handler(commands = ["add"])
async def add(message):
    command = list(message.text.split('\n'))
    if len(command) != 4:
        await message.answer("Задача введена некорректно")
    else:
        date = command[1]
        task = command[2]
        category = command[3]
        await message.answer(f'Задача {task} добавлена в категорию {category} на дату {date}')
        task = command[2]+ ' @ ' + command[3]
        add_todo (date, task)

@dp.message_handler(commands = ["show"])
async def show(message):
    # global category
    command = message.text.split(maxsplit=1)
    date = command[1]
    # text = ""
    if date in tasks:
        await message.answer(date)
        for task in tasks[date]:
            # text = date + "\n" print('- ', task)
            await message.answer("* " + task)
    else:
        await message.answer("Задач на эту дату нет")

@dp.message_handler(commands = ["help"])
async def help(message):
    await message.answer(HELP)

# tasks = {
#     }
#
#
# def add_todo (date, task, category):
#   if date in tasks:
#       tasks[date].append(task, category)
#   else:
#       tasks[date] = [task, category]
#
# @dp.message_handler(commands = ["start"])
# async def start_command(message: types.Message):
#     await message.answer("Привет!")
#
# @dp.message_handler(commands = ["add"])
# async def add(message):
#     command = list(message.text.split())
#     if len(command) < 4:
#         await message.answer("Задача введена некорректно")
#
#     else:
#         date = command[1]
#         task = command[2]
#         category = command[3]
#         await message.answer(f'Задача {task} добавлена в категорию {category} на дату {date}')
#         task = command[2]#+ ' @ ' + command[3]
#         add_todo (date, task, category)
#
#
#
# @dp.message_handler(commands = ["show"])
# async def show(message):
#     # global category
#     command = message.text.split(maxsplit=1)
#     date = command[1]
#     # text = ""
#     if date in tasks:
#         await message.answer(date)
#         for task in tasks[date]:
#             # text = date + "\n" print('- ', task)
#             await message.answer("* ", task, category)
#     else:
#         await message.answer("Задач на эту дату нет")
#
# @dp.message_handler(commands = ["help"])
# async def help(message):
#     await message.answer(HELP)

# @dp.message_handler()
# async def get_password(message: types.Message):
#     passlength = message.text
#     try:
#         passlength = int(passlength)
#         if not 0 < passlength < 74:
#             await message.reply("Недопустимый размер пароля")
#         else:
#             a = 'abcdefghijklmmopqrstuvwxyz'
#             b = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#             c = '0123456789'
#             d = '/_-?!*,$#@%^&'
#
#             all = a + b + c + d
#             password = ''.join(random.sample(all, passlength))
#             await message.answer(f"Ваш пароль: {password}")
#     except Exception as ex2:
#         print(ex2)
#         await message.answer("Необходимо вести числа от 1 до 74")

if __name__ == '__main__':
    executor.start_polling(dp)