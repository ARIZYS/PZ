number = int(input("Введите целое чиcло больше 999"))
while number < 999:
    number = int(input("Ошибка! Заного введите целое чиcло больше 999"))
    win = ((number//100)%10)