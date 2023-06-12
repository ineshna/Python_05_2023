# Напишите программу, генерирующую элементы арифметической прогрессии
# Программа принимает от пользователя три числа :
# - Первый элемент прогрессии, Разность (шаг) и Количество элементов
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# 	Напишите функцию
# 	- Аргументы: три указанных параметра
# 	- Возвращает: список элементов арифмитической прогрессии.
"""
	Примеры/Тесты:
   
	Ввод: 7 2 5
	Вывод: [7 9 11 13 15]
	Ввод: 2 3 12
	Вывод: [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]

```(*)``` **Усложнение.** Для формирования списка внутри функции используйте Comprehension
```(**)``` **Усложнение.** Присвоение значений переменным a1,d,n запишите, используя только один input,
 в одну строку, вам понадобится распаковка и Comprehension или map

"""
def progressia(a1,d,num_el) -> list:
    result = []
    for i in range(num_el):
        an = a1 + i * d
        result.append(an)
    return result
print(progressia(2, 3, 12))