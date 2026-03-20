import pytest
import allure
from praktikum.bun import Bun

class TestBun:
    @allure.title("Возвращается корректное имя булочки")
    @pytest.mark.parametrize("name", [
        "black bun",
        "white bun",
        "red bun"
    ])
    def test_get_name_returns_correct_bun_name(self, name):
        bun = Bun(name, 1000)
        
        assert bun.get_name() == name

    @allure.title("Возвращается корректная цена булочки")
    @pytest.mark.parametrize("price", [
        100,
        999.99,
        1000,
        1500,
        100000
    ])
    def test_get_price_returns_correct_bun_price(self, price):
        bun = Bun("Метеоритный бургер", price)

        assert bun.get_price() == price
