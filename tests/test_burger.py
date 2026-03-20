from unittest.mock import Mock
import allure
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@allure.feature("Burger")
class TestBurger:

    @allure.title("Добавление булочек")
    def test_set_buns_valid_bun_sets_bun(self):
        burger = Burger()
        bun = Bun("Флюоресцентный бургер", 1000)
        burger.set_buns(bun)

        assert burger.bun == bun

    @allure.title("Добавление ингредиентов")
    def test_add_ingredient_adds_ingredients_to_list(self):
        burger = Burger()
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "space sauce", 80)
        burger.add_ingredient(ingredient)

        assert burger.ingredients[0].get_name() == "space sauce"
        assert burger.ingredients[0].get_price() == 80
        assert burger.ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE

    @allure.title("Удаление ингредиентов")
    def test_remove_ingredient_valid_index_removes_ingredient(self):
        burger = Burger()
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "space sauce", 80)
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0

    @allure.title("Перемещение ингредиентов")
    def test_move_ingredient_valid_indexes_moves_ingredient_to_new_position(self):
        burger = Burger()
        ingredient_1 = Ingredient(INGREDIENT_TYPE_SAUCE, "space sauce", 80)
        ingredient_2 = Ingredient(INGREDIENT_TYPE_SAUCE, "spicy-X", 90)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)

        burger.move_ingredient(1, 0) 

        assert burger.ingredients[0] == ingredient_2
        assert burger.ingredients[1] == ingredient_1

    @allure.title("Расчёт стоимости бургера")
    def test_get_price_returns_correct_total_price(self):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 1000

        mock_imgredient1 = Mock()
        mock_imgredient1.get_price.return_value = 80

        mock_imgredient2 = Mock()
        mock_imgredient2.get_price.return_value = 3000

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_imgredient1)
        burger.add_ingredient(mock_imgredient2)

        expected_price = (mock_bun.get_price() * 2) + mock_imgredient1.get_price() + mock_imgredient2.get_price()
        assert burger.get_price() == expected_price

    @allure.title("Проверка формирования чека")
    def test_get_receipt_returns_formatted_receipt(self):
        burger = Burger()

        bun = Bun("Флюоресцентный бургер", 1000)
        burger.set_buns(bun)

        ingredient_1 = Ingredient(INGREDIENT_TYPE_SAUCE, "space sauce", 80)
        ingredient_2 = Ingredient(INGREDIENT_TYPE_FILLING, "beef cutlet", 3000)
        burger.add_ingredient(ingredient_1)
        burger.add_ingredient(ingredient_2)

        expected_receipt = (
            "(==== Флюоресцентный бургер ====)\n"
            "= sauce space sauce =\n"
            "= filling beef cutlet =\n"
            "(==== Флюоресцентный бургер ====)\n\n"
            f"Price: {burger.get_price()}"
        )

        assert burger.get_receipt() == expected_receipt
