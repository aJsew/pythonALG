# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

a = int(input('Введите трехзначное число'))
h = a // 100
d = (a // 10) - (a // 100 * 10)
n = a % 10
sum = h + d + n
multiply = h * d * n
print(sum, multiply)
