from math import*
C = int(input("Ветер="))

match C:
    case 1|2|3|4:print("Слабый")
    case 5|6|7|8|9|10:print("Умеренный")
    case 9|10|11|12|13|14|15|16|17|18:print("Сильный")
    case _:print("Ураганный")
