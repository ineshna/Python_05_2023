# 1.4[8]. Требуется определить, можно ли от шоколадки размером n × m долек 
# отломить k долек, если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).
	# Примеры/Тесты:
	# 3 2 4 -> yes
	# 3 2 1 -> no
n = int(input('Введите число долек по вертикали: '))
m = int(input('Введите число долек по горизонтали: '))
k = int(input('Сколько долек отломить ?'))
if n % k != 0 and m % k != 0:
    print('Столько долек можно отломить')
else :
    print('Неполуичтся отломить столько долек за один раз')