# Дано целое число, большее 999. Используя одну операцию деления нацело и одну
# операцию взятия остатка от деления, найти цифру,
# соответствующуто разряду сотен в записи этого числа.

number = int(input("Введите целое чиcло больше 999:   "))
while number > 999:
    number = int(input("ошибка! Заного введите целое чиcло больше 999:   "))
win = ((number//100)%10)
print(win)
