import logging

# Настройка логирования
logging.basicConfig(filename='warehouse.log', level=logging.INFO, format='%(asctime)s - %(message)s')

class Product:
    def __init__(self, name: str, quantity: int, price: float):
        self.name = name
        self.quantity = quantity
        self.price = price

    def increase_quantity(self, amount: int):
        self.quantity += amount
        logging.info(f'Увеличено количество товара "{self.name}" на {amount}. Текущее количество: {self.quantity}.')

    def decrease_quantity(self, amount: int):
        if amount > self.quantity:
            logging.warning(f'Попытка уменьшить количество товара "{self.name}" на {amount}, но доступно только {self.quantity}.')
            raise ValueError("Недостаточно товара на складе.")
        self.quantity -= amount
        logging.info(f'Уменьшено количество товара "{self.name}" на {amount}. Текущее количество: {self.quantity}.')

    def total_price(self) -> float:
        return self.quantity * self.price


class Warehouse:
    def __init__(self):
        self.products = []

    def add_product(self, product: Product):
        self.products.append(product)
        logging.info(f'Добавлен товар: {product.name}, количество: {product.quantity}, цена: {product.price}.')

    def remove_product(self, product_name: str):
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)
                logging.info(f'Удалён товар: {product.name}.')
                return
        logging.warning(f'Товар "{product_name}" не найден на складе.')

    def total_value(self) -> float:
        return sum(product.total_price() for product in self.products)


class Seller:
    def __init__(self, name: str):
        self.name = name
        self.sales_report = []

    def sell_product(self, warehouse: Warehouse, product_name: str, quantity: int):
        for product in warehouse.products:
            if product.name == product_name:
                product.decrease_quantity(quantity)
                total_cost = product.price * quantity
                self.sales_report.append((product.name, quantity, total_cost))
                logging.info(f'Продавец "{self.name}" продал {quantity} товара "{product.name}".')
                return total_cost
        logging.warning(f'Товар "{product_name}" не найден для продажи.')
        raise ValueError("Товар не найден для продажи.")

    def sales_report_summary(self):
        return self.sales_report


# Пример использования
if __name__ == "__main__":
    warehouse = Warehouse()
    seller = Seller("Иван")

    # Добавление товаров
    warehouse.add_product(Product("Товар A", 100, 10.0))
    warehouse.add_product(Product("Товар B", 50, 20.0))

    # Продавать товары
    try:
        seller.sell_product(warehouse, "Товар A", 10)
    except ValueError as e:
        print(e)

    # Печать отчета о продажах
    print("Отчет о продажах:")
    for item in seller.sales_report_summary():
        print(f"Товар: {item[0]}, Количество: {item[1]}, Выручка: {item[2]}")

    # Расчет общей стоимости товаров на складе
    print(f"Общая стоимость товаров на складе: {warehouse.total_value()}")

    # Удаление товара
    warehouse.remove_product("Товар B")


    ''' Описание:

1. Класс Product: отвечает за товар, его количество и цену с методами увеличения и уменьшения количества, а также расчёта общей стоимости товара.
2. Класс Warehouse: управляет списком товаров, позволяет добавлять и удалять товары, а также рассчитывает общую стоимость всех товаров на складе.
3. Класс Seller: реализует функционал продавца, который может продавать товары и формировать отчёт о продажах.
4. Логирование: все операции логируются в файл `warehouse.log`. '''
