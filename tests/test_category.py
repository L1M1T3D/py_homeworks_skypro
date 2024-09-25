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
