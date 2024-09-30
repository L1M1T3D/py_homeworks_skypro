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
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Выводит список товаров категории"""
        product_list = []
        for i in self.__products:
            product_list.append(f"{i.name}, {int(i.price)} руб., Остаток: {i.quantity} шт.\n")
        return product_list
