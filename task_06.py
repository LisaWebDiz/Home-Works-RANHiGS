# Есть словарь песен 
my_favorite_songs = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}
# Формирование списка из значений словаря:
songs_time = list(my_favorite_songs.values())
#print(songs_time)
# Запрос трех случайных значений из полученного списка:
random_songs_time = choices(songs_time, k=3)
#print(random_songs_time)
total_time = sum(random_songs_time)
#print(total_time)
# В случае, если программа укажет, что помимо минут, в песне в секундах (после точки) указано более 60 секунд:
total_time = str(total_time)
total_time = total_time.split('.')
sum_sec = str(total_time[1]) #количество минут
sum_sec = int(str(sum_sec)[0]) #первый символ количества секунд
#print(int(sum_sec))
# Вывод: Три песни звучат ХХХ минут (общее время звучания трех случайных песен)
if int(sum_sec) >= 6:
  print(f'Три песни звучат {int(total_time[0])+1} минут')
else: print(f'Три песни звучат {int(total_time[0])} минут')
    
# Хорошо
