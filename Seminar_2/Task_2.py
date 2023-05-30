#Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является.
#Т.е. выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
#Примеры/Тесты:
#5 -> в ряду Фибоначчи 5 имеет порядковый номер 6
#6765 -> в в ряду Фибоначчи 6765 имеет порядковый номер 21
#6766 -> -1

#Примечание: Вы можете решить эту задачу, используя формулу чисел Фибоначчи или итеративно.
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711

a = int(input("Введите число :"))
a1 = 0
a2 = 1
a3 = a1 + a2
count = 3
while a > a3:
  a1 = a2
  a2 = a3
  a3 = a1 + a2
  count +=1
if a3 == a:
  print(count)
else:
  print("-1")



