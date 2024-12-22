import collections
import string

def count_unique_words(input_string):
    # Удаляем знаки препинания и приводим строку к нижнему регистру
    translator = str.maketrans('', '', string.punctuation)
    cleaned_string = input_string.translate(translator).lower()
    
    # Разбиваем строку на слова
    words = cleaned_string.split()
    
    # Используем Counter для подсчета уникальных слов
    word_counter = collections.Counter(words)
    
    # Возвращаем количество уникальных слов
    return len(word_counter)

# Пример использования функции
input_str = "Hello, world! Hello, Python; Python is great."
unique_count = count_unique_words(input_str)
print(f"Количество уникальных слов: {unique_count}")


'''
1. Импортируем необходимые модули:
   - `collections`: для использования `Counter`.
   - `string`: для доступа к спискам знаков препинания.

2. Функция `count_unique_words(input_string)`:
   - Удаляет знаки препинания с помощью `str.translate()` и переводит строку в нижний регистр для унификации.
   - Разбивает строку на слова с помощью метода `split()`.
   - Создает `Counter`, который подсчитывает количество каждого уникального слова.
   - Возвращает количество уникальных слов, получая длину объекта `Counter`.


