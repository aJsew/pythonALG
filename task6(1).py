#6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

let_num = int(input('Введите номер буквы'))
num = 97 - 1 + let_num
output = chr(num)
print(output)

