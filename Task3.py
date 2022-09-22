""" Создайте программу для игры в ""Крестики-нолики"".

Пример интерфейса:

   |   | 0
-----------    
   |   |
-----------
   | X |
Ввод можно реализовать через введение двух чисел (номеров строки и столбца). """

# !!!! не доделана

line1 = []
line2 = []
line3 = []



# line = line1
# line1.insert(x,n)
for i in range(1,10):
   n = str(input('Введите X или 0: '))
   y = int(input('Введите номер строки от 1 до 3: '))
   x = int(input('Введите номер столбца от 1 до 3: '))
   if y == 1:
      line = line1
      line1.insert(x-1, n)
      print(line1)
   elif y == 2:
      line = line2
      line2.insert(x-1, n)
   else:
      line = line3
      line3.insert(x-1, n)
   row1 = ' | '.join(line1)
   row2 = ' | '.join(line2)
   row3 = ' | '.join(line3)
   print(row1)
   print('----------')
   print(row2)
   print('-----')
   print(row3)


