# Требуется найти в списке целых чисел самый близкий по величине элемент
# к заданному числу X.  Пользователь вводит это число с клавиатуры, 
# список можно считать заданным. Введенное число не обязательно 
# содержится в списке.
"""
    Примеры/Тесты:
    Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
    Output: 2
    Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9
"""
# list_1 = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
# x = int(input('Введите число:'))
#print(min(list_1, key=lambda a:abs(a-x)))
#b=[abs(list_1[i]-x) for i in range(len(list_1))]
list_1 = [1,3,6,3,5,67,2,2,4,89,-9,3]
x = int(input("Введите число X: "))

min_diff = abs(x - list_1[0]) #считаем для 0го элемента расстояние до Х
index_min_diff = 0
for num in range(1,len(list_1)):
 if min_diff > abs(x-list_1[num]):
     min_diff = abs(x-list_1[num])
     index_min_diff = num
print(f'На позиции {index_min_diff} в списке находится самый близкий к {x} элемент и он равен {list_1[index_min_diff]}')