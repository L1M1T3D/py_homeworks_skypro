class Product:
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
        self.quantity = quantity

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
        """Помогает посчитать итоговую стоимость, исходя из количества и стоимости 1 штуки товара"""
        return (self.price * self.quantity) + (other.price * other.quantity)
