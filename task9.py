# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = int(input('Введите число, отличное от остальных'))
b = int(input('Введите число, отличное от остальных'))
c = int(input('Введите число, отличное от остальных'))

if a > b:
    if a > c:
        if b > c:
            print(b)
        else:
            print(c)
    else:
        print(a)
else:
    if b > c:
        if a > c:
            print(a)
        else:
            print(c)
    else:
        print(b)