# Напишите функцию, которая принимает число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя нацело:
# 1 и само число
# Если число простое - функция возвращает True, если нет - возвращает False
"""
Примеры/Тесты:
<function_name>(13) -> True
<function_name>(10) -> False
"""
# def simple_num(number):
#     i = 0
#     for devider in range(2,number//2 +1):
#         if number % devider ==0:
#             i += 1

#     if i>=1:
#         return False
#     else:
#         return True
#     print(simple_num(10))

def simple_num(number):
    for devider in range(2,number//2 +1):
        if number % devider ==0:
            return False
    return True

print(simple_num(13))