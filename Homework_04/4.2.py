import itertools
import time

def infinite_generator():
    """Создание бесконечного генератора чисел, начиная с 0"""
    for i in itertools.count():
        yield i

def apply_function_to_iterator(iterator, function):
    """Применение функции к каждому элементу в итераторе"""
    try:
        for item in iterator:
            print(function(item))  # Применение функции
    except StopIteration:
        print("Итератор завершен.")

def combine_iterators(*iterators):
    """Объединение нескольких итераторов в один"""
    combined_iterator = itertools.chain(*iterators)
    return combined_iterator

def main():
    # Задача 1: Создание бесконечного генератора и применение к первым 10 элементам квадрата
    print("Бесконенный генератор чисел:")
    gen = infinite_generator()
    apply_function_to_iterator(itertools.islice(gen, 10), lambda x: x**2)  # Применение функции (квадрат)

    # Задача 2: Объединение нескольких итераторов
    print("\nОбъединение нескольких итераторов:")
    it1 = itertools.chain(range(5))  # Итератор 1: 0, 1, 2, 3, 4
    it2 = itertools.chain(range(5, 10))  # Итератор 2: 5, 6, 7, 8, 9

    combined_it = combine_iterators(it1, it2)
    
    # Вывод объединенного итератора
    try:
        apply_function_to_iterator(combined_it, lambda x: x)  # Применяем функцию (идентичную)
    except StopIteration:
        print("Объединенный итератор завершен.")

if __name__ == "__main__":
    main()
'''


1. **Создание бесконечного генератора**:
   - Функция `infinite_generator()` использует `itertools.count()`, чтобы создать бесконечный генератор чисел, начиная с 0.

2. **Применение функций к каждому элементу в итераторе**:
   - Функция `apply_function_to_iterator()` принимает итератор и функцию как аргументы. Она применяет заданную функцию ко всем элементам итератора и выводит результаты. Также она обрабатывает исключение `StopIteration`, чтобы предотвратить ошибку при завершении итератора.

3. **Объединение нескольких итераторов**:
   - Функция `combine_iterators()` использует `itertools.chain()` для объединения нескольких итераторов в один.

4. **Основная функция (`main()`)**:
   - Создается бесконечный генератор, и к первым 10 элементам применяется функция квадратирования.
   - Создаются два итератора, которые объединяются с помощью `combine_iterators()`, а затем применяется функция к каждому элементу объединенного итератора.

'''
