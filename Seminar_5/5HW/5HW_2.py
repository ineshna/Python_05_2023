
#Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых 
#неотрицательных чисел. Из всех арифметических операций допускаются только +1 
#и -1. Циклы использовать нельзя
"""
	Примеры/Тесты:
    <function_name>(0,0) -> 0
    <function_name>(0,2) -> 2
    <function_name>(3,0) -> 3
"""
# a = int(input("Введите первое слагаемое :"))
# b = int(input("Введите второе слагаемое:"))
# def suma(a, b):
#     if b==0:
#         return a
#     return suma(a+1,b-1)
# print(suma(a,b))

def suma(a, b):
    if b==0:
        return a
    return suma(a+1,b-1)
print(suma(0,0))
print(suma(0,2))
print(suma(3,0))