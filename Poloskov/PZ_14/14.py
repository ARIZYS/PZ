import re

# Открываем исходный файл для чтения
with open('ip_address.txt', 'r') as f:
    lines = f.readlines()

# Открываем два новых файла для записи
with open('first_file.txt', 'w') as f1, open('second_file.txt', 'w') as f2:
    # Перебираем строки из исходного файла
    for line in lines:
        # Ищем в строке IP-адрес с нулевым четвертым октетом
        match = re.search(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.0\b', line)
        if match:
            # Если нашли, записываем строку в первый файл
            f1.write(line)
        else:
            # Если не нашли, записываем строку во второй файл
            f2.write(line)

# Подсчитываем количество строк в каждом файле
with open('first_file.txt', 'r') as f1, open('second_file.txt', 'r') as f2:
    count1 = len(f1.readlines())
    count2 = len(f2.readlines())
    print(f'Количество строк в первом файле: {count1}')
    print(f'Количество строк во втором файле: {count2}')
