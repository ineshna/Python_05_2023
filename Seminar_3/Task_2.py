# Дана последовательность из N целых чисел и число K. 
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на 
# K элементов вправо, K – положительное число.

#Примечание: Пользователь может вводить значения списка или список задан изначально.

#Примеры/Тесты:
#Input: [1, 2, 3, 4, 5] k = 3
#Output: [4, 5, 1, 2, 3]
list_1 = [1, 2, 3, 4, 5]
k = int(input('Введите число :'))
resul_list =[]
resul_list = list_1[k:] + list_1[:k]
print(list_1)
print(resul_list)