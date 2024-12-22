def read_numeric_lines(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()  # Удаляем лишние пробелы
                # Проверяем, является ли строка числом
                if line.replace('.', '', 1).isdigit() or (line.startswith('-') and line[1:].replace('.', '', 1).isdigit()):
                    print(line)
                else:
                    raise TypeError(f'Некорректное значение в строке: {line}')
    except FileNotFoundError:
        print(f'Ошибка: файл {filename} не найден.')
    except TypeError as e:
        print(e)

# Пример вызова функции
# read_numeric_lines('data.txt')


''' Описание функции:

1. Функция `read_numeric_lines(filename)`:
   - Принимает имя файла и открывает его для чтения.
   - Использует цикл для чтения строк из файла по одной.
   - Метод `strip()` удаляет лишние пробелы по краям каждой строки.
   - Проверяет, является ли строка числом:
     - Для положительных чисел использует метод `isdigit()`.
     - Для отрицательных чисел учитывает знак `'-'`.
   - Если строка не является числом, выбрасывается исключение `TypeError`.
2. Обработка исключений:
   - `FileNotFoundError` обрабатывается для ситуации, когда файл не найден.
   - `TypeError` обрабатывается, если в файле найдена некорректная строка.
'''
