class DataBuffer:
    def __init__(self):
        self.buffer = []  # Инициализация пустого буфера

    def add_data(self, data):
        """
        Добавляет данные в буфер.
        Если в буфере уже есть хотя бы 5 элементов, выводит сообщение о переполнении и очищает буфер.
        """
        self.buffer.append(data)  # Добавляем данные в буфер
        if len(self.buffer) >= 5:  # Проверяем, достигнут ли лимит
            print("Буфер переполнен. Очищаем буфер.")
            self.buffer.clear()  # Очищаем буфер

    def get_data(self):
        """
        Возвращает данные из буфера.
        Если буфер пуст, выводит сообщение об отсутствии данных.
        """
        if not self.buffer:  # Проверяем, пуст ли буфер
            print("Буфер пуст. Нет данных для получения.")
            return None
        else:
            return self.buffer  # Возвращаем данные из буфера

# Пример использования класса
if __name__ == "__main__":
    buffer = DataBuffer()

    # Добавляем данные в буфер
    buffer.add_data(1)
    buffer.add_data(2)
    buffer.add_data(3)
    buffer.add_data(4)
    buffer.add_data(5)  # Буфер переполнен, очищается

    # Получаем данные из буфера
    print("Данные из буфера:", buffer.get_data())  # Буфер пуст

    # Добавляем новые данные
    buffer.add_data(6)
    buffer.add_data(7)

    # Получаем данные из буфера
    print("Данные из буфера:", buffer.get_data())  # Возвращает [6, 7]
