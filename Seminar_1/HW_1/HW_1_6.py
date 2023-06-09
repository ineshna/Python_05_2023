"""
#### 1.3[6]. Вы пользуетесь общественным транспортом? Вероятно, 
вы расплачивались за проезд и получали билет с номером.Счастливым билетом
называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме 
последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
Вам требуется написать программу, которая проверяет счастливость билета.

	Примеры/Тесты:
	385916 >>> yes
	123456 >>> no

```(*)``` **Усложнение.** Вывод результат на экран сделайте одной строкой
 (только один print), для этого используйте тернарный оператор
"""
ticket = int(input("Введите шестизначный номер билета :"))
i = 3
sumR = 0
sumL = 0
while i > 0 :
 sum1 = ticket % 10  
 ticket = (ticket - sum1) // 10
 i -= 1
 sumR += sum1
i = 3
while i > 0 :
 sum2 = ticket % 10  
 ticket = (ticket - sum2) // 10
 i -= 1
 sumL += sum2
if sumR == sumL:
 print("Ура! счастивый билетик!")
else:
 print("Нормальный билетик")