# 7. По длинам трех отрезков, введенных пользователем, определить возможность 
# существования треугольника, составленного из этих отрезков. 
# Если такой треугольник существует, то определить, 
# является ли он разносторонним, равнобедренным или равносторонним.

a = int(input('Введите длину отрезка'))
b = int(input('Введите длину отрезка'))
c = int(input('Введите длину отрезка'))
if a > b:
    if a > c:
        if (b + c) > a:
            print('Существует')
            e = 1
        else:
            print('Не существует')
            e = 0
    else:
        if (a + b) > c:
            print('Существует')
            e = 1
        else:
            print('Не существует')
            e = 0
else:
    if b > c:
        if (a + c) > b:
            print('Существует')
            e = 1
        else:
            print('Не существует')
            e = 0
    else:
        if (a + b) > c:
            print('Существует')
            e = 1
        else:
            print('Не существует')
            e = 0
if e == 1:
    if a == b:
        if a == c:
            print('Равносторонний')
        else:
            print('Равнобедренный')
    else:
        if a == c:
            print('Равнобедренный')
        else:
            print('Разносторонний')