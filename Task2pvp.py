""" Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. 
Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. 
За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. 
Сколько конфет нужно взять первому игроку, 
чтобы забрать все конфеты у своего конкурента?

a) Добавьте игру против бота. 
Достаточно сделать так, чтобы бот не брал конфет 
больше положенного или больше чем имеется в куче.

b) Подумайте как наделить бота ""интеллектом"". 
Напоминаю, если перед пользователем будет лежать 29 конфет, 
то он, однозначно, проиграет. Достаточно довести игру до такой 
ситуации. """
import random
candy = 2021
p1 = 'Player1'
p2 = 'Player2'
print('Жеребъёвка...')
p = random.randint(1, 3)
print(random.randint(1, 3))
if p == 1:
    p = p1
else:
    p = p2
print(f'Начинает {p}')

while candy > 28:
    n = int(input(f'Ваш ход {p}: '))
    if n > 28 or n <= 0:
        print('Количество взятых конфет должно быть в промежутке от 1 до 28')
    else:
        candy = candy - n
        print(candy)
        if p == p1:
            p = p2
        else:
            p = p1

print(f'Победил {p}')
