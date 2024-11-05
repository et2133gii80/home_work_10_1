import pytest

from src.category import Category
from src.mixin_log import MixinLog
from src.product import Product
from tests.conftest import smartphone, product_1

new_product = Product.new_product(
    {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }
)


def test_category_tv(category_tv, product_4):
    assert category_tv.name == "Телевизоры"
    assert (
        category_tv.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert category_tv.products == [product_4]


def test_category_smart(category_smart, product_1, product_2, product_3):
    assert category_smart.name == "Смартфоны"
    assert (
        category_smart.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category_smart.products == [product_1, product_2, product_3]


def test_category(category_smart, product_4):
    category_smart.add_product(product_4)
    category_smart.add_product(new_product)
    assert Category.product_count == 9


product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)

new_product = Product.new_product(
    {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }
)


def test_samsung(product_samsung):
    assert product_samsung.name == "Samsung Galaxy S23 Ultra"
    assert product_samsung.description == "256GB, Серый цвет, 200MP камера"
    assert product_samsung.price == 180000.0
    assert product_samsung.quantity == 5


def test_iphone(product_iphone):
    assert product_iphone.name == "Iphone 15"
    assert product_iphone.description == "512GB, Gray space"
    assert product_iphone.price == 210000.0
    assert product_iphone.quantity == 8


def test_new_product():
    new_product.price = 0
    assert new_product.price == 180000
    new_product.price = 12000
    assert new_product.price == 12000


# тесты для дз "магические методы"
def test_str_product(product_1, product_2):
    assert product_1.__str__() == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert product_2.__str__() == "Iphone 15, 210000.0 руб. Остаток: 8 шт."


def test_category_getter(category_smart):
    assert category_smart.product == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
        "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"
    )


def test_str_category(category_smart):
    assert category_smart.__str__() == "Смартфоны, количество продуктов: 27 шт."


def test_add_product(product_1, product_2):
    assert product_1 + product_2 == 2580000.0


def test_smartphone(smartphone):
    assert smartphone.efficiency == 95.5
    assert smartphone.color == "Серый"
    assert smartphone.memory == 256
    assert smartphone.model == "S23 Ultra"


def test_glass(grass):
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зеленый"


def test_add_products(smartphone, grass):
    with pytest.raises(TypeError):
        assert smartphone + grass


def test_isinstance(category_tv):
    with pytest.raises(TypeError):
        assert category_tv.add_product()


def test_abc(abc):
    assert abc.name == "Samsung Galaxy S23 Ultra"
    assert abc.description == "256GB, Серый цвет, 200MP камера"
    assert abc.quantity == 5


def test_mixin_product(product1):
    assert product1.__repr__() == "Product (Samsung Galaxy S23 Ultra, 256GB, Серый цвет, 200MP камера, 180000.0, 5)"


def test_raises():
    with pytest.raises(ValueError) as ex:
        quantity_zero = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 0)
        assert quantity_zero == f"{ex}: Товар с нулевым количеством не может быть добавлен"


def test_average_price(category_smart):
    assert category_smart.average_price() == 140333.3


def test_average_price_with_zero_products(category_zero):
    assert category_zero.average_price() == 0
