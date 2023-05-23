# Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) 
num = int(input('Ведите трехзначное число :'))
summa = 0
while num > 0 :
 result = num % 10  
 num = (num - result) // 10
 summa += result
print('Cумма цифр равна :' , summa)