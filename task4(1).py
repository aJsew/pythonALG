import random
# 4. Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ. 
# Для каждого из трех случаев пользователь задает свои границы диапазона. 
# Например, если надо получить случайный символ от 'a' до 'f', 
# то вводятся эти символы. Программа должна вывести на экран любой символ алфавита
# от 'a' до 'f' включительно.

min = input('Минимальная граница')
max = input('Максимальная граница')
if not min.isalpha():
    if float(min) == (float(min) // 1):
        min = int(min)
        max = int(max)
        output = random.randint(min, max)
    else:
        min = float(min)
        max = float(max)
        output = random.uniform(min, max)
else:
    output = chr(random.randint(ord(min), ord(max)))
print(output)