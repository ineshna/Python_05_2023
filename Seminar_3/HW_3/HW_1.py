# Дан список целых чисел.  Требуется вычислить, сколько раз встречается 
# некоторое число X в этом списке.
# Пользователь вводит число X с клавиатуры. Список можно считать 
# заданным.
# Если такого числа в списке нет - вывести -1.

#	Примеры/Тесты:
#    Input:   [10, 5, 7, 3, 3, 0, 5, 7, 2, 8], x = 3
#    Output:  2

#    Input:   [10, 5, 7, 3, 3, 0, 5, 7, 2, 8], x = 20
#    Output:  -1
#Напишите алгоритм подсчета самостоятельно или воспользуйтесь методами списка.

#```(*)``` **Усложнение.** При выводе результата на экран воспользуйтесь 
# тернарным оператором.
list_1 = [10, 5, 7, 3, 3, 0, 5, 7, 2, 8]
x = int(input('Введите искомое число :'))
result = 0
# for i in list_1:
#       if x not in list_1:
#            result = -1
# print(result)

for i in list_1:
     if x == i:
        result += 1
     else:
      result = -1
print(result)

#print(list_1.count(x))

