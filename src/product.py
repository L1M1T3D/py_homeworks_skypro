from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный класс для продуктов"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def price(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __str__(self):
        pass


class MixinLog:
    """Класс для показа информации об объекте"""

    def __init__(self, *args, **kwargs):
        print(f"{self.__class__.__name__}({args})")
        super().__init__()


class Product(MixinLog, BaseProduct):
    """Класс для добавления нового продукта"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод для инициализации экземпляра класса"""
        self.name = name
        self.description = description
        self.__price = price
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        else:
            self.quantity = quantity
        super().__init__(name, description, price, quantity)

    @classmethod
    def new_product(cls, product, category=None):
        """Метод возвращает объект класса Product, но сперва проходит проверку на уникальность"""
        for i in category.products:
            i = i.split(",")
            if product["name"].lower() == i[0].lower():
                print("В категории уже имеется такой товар.")
        else:
            return cls(product["name"], product["description"], product["price"], product["quantity"])

    @property
    def price(self):
        """Возвращает цену товара"""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Изменяет цену товара, но сперва проходит проверку на отрицательную/нулевую цену и на подтверждение
        снижения цены"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            user_input = input("Цена товара снижается. Вы готовы подтвердить действие? (y/n)\n")
            if user_input.lower() == "y":
                print("Вы установили новую цену.")
                self.__price = new_price
            elif user_input.lower() == "n":
                print("Вы отменили действие.")
        elif new_price > self.__price:
            self.__price = new_price

    def __str__(self):
        """Возвращает информацию о продукте"""
        return f"{self.name}, {int(self.price)} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Помогает посчитать итоговую стоимость, исходя из количества и стоимости 1 шт. товара"""
        if type(self) is not type(other):
            raise TypeError(f"Нельзя сложить {self.__class__.__name__} и {other.__class__.__name__}")
        return (self.price * self.quantity) + (other.price * other.quantity)


class Smartphone(Product):
    """Класс для продукта - Смартфона"""

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс для продукта - Трава газонная"""

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
