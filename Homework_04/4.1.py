import datetime

def display_current_datetime():
    # Отображение текущей даты и времени
    current_datetime = datetime.datetime.now()
    print(f"Текущая дата и время: {current_datetime}")

def calculate_date_difference(date1, date2):
    # Вычисление разницы между двумя датами
    delta = date2 - date1
    print(f"Разница между {date2.date()} и {date1.date()} составляет {delta.days} дней.")

def convert_string_to_datetime(date_string, date_format):
    # Преобразование строки в объект даты и времени
    try:
        converted_date = datetime.datetime.strptime(date_string, date_format)
        print(f"Преобразованная дата: {converted_date}")
        return converted_date
    except ValueError as e:
        print(f"Ошибка преобразования: {e}")

def main():
    # Отображение текущей даты и времени
    display_current_datetime()
    
    # Задание двух дат для вычисления разницы
    date_str1 = "2023-10-01"
    date_str2 = "2023-10-15"
    
    # Преобразование строк в объекты даты
    date_format = "%Y-%m-%d"
    date1 = convert_string_to_datetime(date_str1, date_format)
    date2 = convert_string_to_datetime(date_str2, date_format)
    
    # Вычисление разницы между двумя датами
    if date1 and date2:
        calculate_date_difference(date1, date2)

if __name__ == "__main__":
    main()

'''

2. **Функция `display_current_datetime`**:
   - Эта функция использует `datetime.datetime.now()` для получения текущей даты и времени и выводит результат на экран.

3. **Функция `calculate_date_difference`**:
   - Аргументами функции являются две даты. Она вычисляет разницу между ними, используя простой вычет, и выводит количество дней между этими датами.

4. **Функция `convert_string_to_datetime`**:
   - Преобразует строку в объект даты с помощью метода `strptime()`, который принимает строку и формат даты. Если преобразование не удается, выводится сообщение об ошибке.

5. **Функция `main`**:
   - Основная логика программы выполняется здесь. Мы сначала отображаем текущее время, затем задаем две строки с датами, преобразуем их и, в конце концов, вычисляем разницу.

'''
