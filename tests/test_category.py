import pytest

from src.category import Category
from src.product import Product


@pytest.fixture(autouse=True)
def reset_counters():
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def category():
    return Category(
        "Смартфоны",
        "Отличный вид коммуникации с родными",
        [Product("Realme 11 Pro", "256GB", 18000.0, 5), Product("Iphone 13 Pro", "128GB, Gray, eSim", 120000.0, 3)],
    )


def test_init(category):
    assert category.name == "Смартфоны"
    assert category.description == "Отличный вид коммуникации с родными"
    assert len(category.products) == 2


def test_category_count(category):
    assert Category.category_count == 1


def test_products_count(category):
    assert Category.product_count == 2


def test_multiple_categories():
    category1 = Category(
        "Смартфоны",
        "Отличный вид коммуникации с родными",
        [Product("Realme 11 Pro", "256GB", 18000.0, 2), Product("Iphone 13 Pro", "128GB", 120000.0, 1)],
    )
    category2 = Category("Автомобили", "Лучшие во всём городе", [Product("Toyota", "RAV4", 4000000.0, 1)])
    assert category1.name == "Смартфоны"
    assert category2.name == "Автомобили"
    assert Category.category_count == 2
    assert Category.product_count == 3


def test_empty_category():
    empty_category = Category("Пусто", "Тут ничего нет", [])
    assert empty_category.name == "Пусто"
    assert empty_category.description == "Тут ничего нет"
    assert len(empty_category.products) == 0


def test_add_product():
    product1 = Product(name="Продукт", description="Описание", price=100.0, quantity=10)
    product2 = Product(name="Ещё продукт", description="Описание", price=200.0, quantity=5)
    category = Category(name="Категория", description="Описание", products=[product1])
    category.add_product(product2)
    assert len(category.products) == 2
    assert Category.product_count == 2
    assert "Ещё продукт" in category.products[1]


def test_products_property():
    product1 = Product(name="Продукт", description="Описание", price=100.0, quantity=10)
    product2 = Product(name="Ещё продукт", description="Описание", price=200.0, quantity=5)
    category = Category(name="Категория", description="Описание", products=[product1, product2])
    product_list = category.products
    assert len(product_list) == 2
    assert "Продукт" in product_list[0]
    assert "Ещё продукт" in product_list[1]


def test_category_str():
    product1 = Product(name="Product1", description="Описание", price=100.0, quantity=10)
    product2 = Product(name="Ещё продукт", description="Описание", price=200.0, quantity=5)
    category = Category(name="Категория", description="Описание", products=[product1, product2])

    expected_output = "Категория, количество продуктов: 15 шт."
    assert str(category) == expected_output


def test_category_products_str():
    product1 = Product(name="Продукт", description="Описание", price=100.0, quantity=10)
    product2 = Product(name="Продукт", description="Описание", price=200.0, quantity=5)
    category = Category(name="Категория", description="Описание", products=[product1, product2])

    product_list = category.products
    assert len(product_list) == 2
    assert product_list[0] == str(product1)
    assert product_list[1] == str(product2)


def test_add_product_to_category():
    product = Product(name="Продукт", description="Описание", price=100.0, quantity=10)
    category = Category(name="Категория", description="Описание", products=[])

    category.add_product(product)
    assert len(category.products) == 1
    assert str(category.products[0]) == "Продукт, 100 руб. Остаток: 10 шт."


def test_add_invalid_product_type():
    category = Category(name="Категория", description="Описание", products=[])

    with pytest.raises(TypeError):
        category.add_product("Не_продукт")
