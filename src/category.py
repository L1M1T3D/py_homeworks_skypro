from src.product import Product


class Category:
    """Класс для управления категориями."""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """Метод для инициализации экземпляра класса. Также управление атрибутами класса"""
        self.name = name
        self.description = description
        self.__products = products
        Category.product_count += len(products)
        Category.category_count += 1

    def add_product(self, product):
        """Добавляет товар в категорию"""
        if not issubclass(product.__class__, Product):
            raise TypeError("Вам нельзя добавлять что-то другое в категорию, кроме продуктов!")
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Выводит список товаров категории"""
        return [str(i) for i in self.__products]

    def __str__(self):
        """Возвращает информацию о категории и количестве товаров на складе"""
        total_quantity = sum([product.quantity for product in self.__products])
        return f"{self.name}, количество продуктов: {total_quantity} шт."
