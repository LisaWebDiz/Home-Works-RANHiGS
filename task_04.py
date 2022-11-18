import random

# Приведен плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
my_favorite_songs = [
  ['Waste a Moment', 3.03], 
  ['New Salvation', 4.02], 
  ['Staying\' Alive', 3.40], 
  ['Out of Touch', 3.03], 
  ['A Sorta Fairytale', 5.28], 
  ['Easy', 4.15], 
  ['Beautiful Day', 4.04], 
  ['Nowhere to Run', 2.58], 
  ['In This World', 4.02]]
  
random_songs = random.choices(my_favorite_songs, k=3)
print(random_songs)
sum = 0
for time in random_songs:
  time = time[1]
  sum += time
#print(float(round(sum, 2)))
# В случае, если программа укажет, что помимо минут, в песне в секундах (после точки) указано более 60 секунд:
sum = str(sum)
sum_min_sec = sum.split('.')
sum_sec = str(sum_min_sec[1])
sum_sec = int(str(sum_sec)[0])
#print(int(sum_sec))
if int(sum_sec) >= 6:
  print(f'Три песни звучат {int(sum_min_sec[0])+1} минут')
else: print(f'Три песни звучат {int(sum_min_sec[0])} минут')
  
# Хорошо.
# Только choices() к сожалению может выдавать повторы. 
# Попробуйте потом sample(
# Пример
# Решение 2
time = 0
for song in sample(my_favorite_songs, 3):
    print(song[0])
    time += song[1]

print(f'Три песни звучат {round(time, 2)}')
