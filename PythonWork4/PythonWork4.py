﻿#1.4[8]. Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
#если разрешается сделать один разлом по прямой между дольками 
#(то есть разломить шоколадку на два прямоугольника).
#Примеры/Тесты:
#3 2 4 -> yes
#3 2 1 -> no

n = int(input('Ширина дольки '))
m = int(input('Длина дольки '))
k = int(input('отломить долек '))

if (n * m) % k == 0:
    print("no")
else:
    print('yes')
