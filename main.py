spis = input("Введите строку: ") # Запрашивает у пользователя ввод строки

glas = 0 # Инициализирует счетчик гласных
sogl = 0 # Инициализирует счетчик согласных
length = 0 # Подсчитывает количество символов в строке

all_glas = "аеёиоуыэюя" # Определяет список всех гласных
all_sogl = "бвгджзйклмнпрстфхцчшщ" # Определяет список всех согласных
for char in spis: # Цикл проходит по каждому символу в строке
    if char != " ":  # Пропускает пробелы
        length += 1  # Увеличивает счетчик символов (кроме пробелов)
        if char in all_glas: # Проверяет, является ли символ гласной
            glas += 1 # Увеличивает счетчик гласных на 1
        elif char in all_sogl: # Проверяет, является ли символ согласной
            sogl += 1 # Увеличивает счетчик согласных на 1

print('Количество гласных', glas) # Выводит количество гласных
print('Количество согласных', sogl) # Выводит количество согласных
print('Количество букв в строке', length) # Выводит количество символов
