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


def test_price_setter_negative_or_zero():
    product = Product(name="Продукт", description="Описание", price=100.0, quantity=10)
    product.price = -50
    assert product.price == 100.0
    product.price = 0
    assert product.price == 100.0


def test_price_setter_reduction(mocker):
    product = Product(name="Продукт", description="Описание", price=100.0, quantity=10)
    mocker.patch("builtins.input", return_value="y")
    product.price = 50
    assert product.price == 50
    mocker.patch("builtins.input", return_value="n")
    product.price = 25
    assert product.price == 50


def test_new_product_creation():
    category = type("Категория", (), {"products": []})
    product_data = {"name": "Новый продукт", "description": "Это новый продукт", "price": 150.0, "quantity": 5}
    new_product = Product.new_product(product_data, category=category)
    assert new_product.name == "Новый продукт"
    assert new_product.price == 150.0


def test_new_product_uniqueness_check(capsys):
    category = type("Категория", (), {"products": ["Новый продукт, 150 руб. Остаток: 5 шт.\n"]})
    product_data = {"name": "Новый продукт", "description": "Это новый продукт", "price": 150.0, "quantity": 5}
    Product.new_product(product_data, category=category)
    captured = capsys.readouterr()
    assert "В категории уже имеется такой товар." in captured.out


def test_product_str():
    product = Product(name="Продукт", description="Описание", price=100.0, quantity=10)

    expected_output = "Продукт, 100 руб. Остаток: 10 шт."
    assert str(product) == expected_output


def test_product_addition():
    product1 = Product(name="Продукт", description="Описание", price=100.0, quantity=2)
    product2 = Product(name="Ещё продукт", description="Описание", price=200.0, quantity=3)

    total_value = (product1.price * product1.quantity) + (product2.price * product2.quantity)
    assert product1 + product2 == total_value
