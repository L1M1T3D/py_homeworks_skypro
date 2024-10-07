import pytest

from src.product import LawnGrass, Product, Smartphone


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


def test_product_price_addition():
    product1 = Product(name="Продукт", description="Описание", price=100.0, quantity=2)
    product2 = Product(name="Ещё продукт", description="Описание", price=200.0, quantity=3)

    total_value = (product1.price * product1.quantity) + (product2.price * product2.quantity)
    assert product1 + product2 == total_value


def test_product_addition():
    product1 = Product(name="Продукт", description="Описание", price=100.0, quantity=2)
    product2 = Product(name="Ещё продукт", description="Описание", price=50.0, quantity=4)

    result = product1 + product2
    assert result == 400.0


def test_product_addition_type_error():
    product1 = Product(name="Продукт", description="Описание", price=100.0, quantity=2)
    smartphone = Smartphone(
        name="Xiaomi",
        description="Описание",
        price=500.0,
        quantity=1,
        efficiency=8,
        model="X100+ Ultra",
        memory=128,
        color="Black",
    )

    with pytest.raises(TypeError):
        product1 + smartphone


def test_smartphone_creation():
    smartphone = Smartphone(
        name="Смартфон",
        description="Самый новый и мощный",
        price=500.0,
        quantity=3,
        efficiency=8,
        model="iPhone",
        memory=128,
        color="Black",
    )

    assert smartphone.name == "Смартфон"
    assert smartphone.description == "Самый новый и мощный"
    assert smartphone.price == 500.0
    assert smartphone.quantity == 3
    assert smartphone.efficiency == 8
    assert smartphone.model == "iPhone"
    assert smartphone.memory == 128
    assert smartphone.color == "Black"


def test_lawngrass_creation():
    lawn_grass = LawnGrass(
        name="Газонная трава",
        description="Для зелёной лужайки",
        price=20.0,
        quantity=50,
        country="USA",
        germination_period=30,
        color="Green",
    )

    assert lawn_grass.name == "Газонная трава"
    assert lawn_grass.description == "Для зелёной лужайки"
    assert lawn_grass.price == 20.0
    assert lawn_grass.quantity == 50
    assert lawn_grass.country == "USA"
    assert lawn_grass.germination_period == 30
    assert lawn_grass.color == "Green"
