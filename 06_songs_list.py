# -*- coding: utf-8 -*-

# Есть список песен группы Depeche Mode со временем звучания с точностью до долей минут

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
#   Три песни звучат ХХХ минут
# Обратите внимание, что делать много вычислений внутри print() - плохой стиль.
# Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz)

song_halo = violator_songs_list[3][1]
song_enjoy_the_silence = violator_songs_list[5][1]
song_clean = violator_songs_list[8][1]
sum_third_songs = song_halo + song_enjoy_the_silence + song_clean

print('Три песни звучат ' + str(round(sum_third_songs, 2)) + ' минут')

# Есть словарь песен группы Depeche Mode
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

# распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
#   А другие три песни звучат ХХХ минут

song_sweetest_perfection = violator_songs_dict['Sweetest Perfection']
song_policy_of_truth = violator_songs_dict['Policy of Truth']
song_blue_dress = violator_songs_dict['Blue Dress']

sum_another_three_songs = song_sweetest_perfection + song_policy_of_truth + song_blue_dress

print('А другие три песни звучат ' + str(round(sum_another_three_songs, 2)) + ' минут')
