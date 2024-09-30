import pytest

from src.product import Product


@pytest.fixture
def product_1():
    return Product("Realme 11 Pro", "256GB", 18000.0, 5)


@pytest.fixture
def product_2():
    return Product("Iphone 13 Pro", "128GB, Gray, eSim", 120000.0, 3)


def test_init(product_1):
    assert product_1.name == "Realme 11 Pro"
    assert product_1.description == "256GB"
    assert product_1.price == 18000.0
    assert product_1.quantity == 5


def test_init_2(product_2):
    assert product_2.name == "Iphone 13 Pro"
    assert product_2.description == "128GB, Gray, eSim"
    assert product_2.price == 120000.0
    assert product_2.quantity == 3
