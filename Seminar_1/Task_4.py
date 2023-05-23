#Дано натуральное число.
#Требуется определить, является ли год с данным номером високосным
year = int(input("Введите год :"))

# print('Yes') if year % 4 ==0 and year % 400 == 0 or year % 400 == 0 else print ('No')

condition1 = year % 4 == 0 and year % 100 != 0
condition2 = year % 400 == 0
if condition1 or condition2:
    print ('Yes')
else:
    print("No")