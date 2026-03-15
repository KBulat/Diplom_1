import allure
import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@allure.feature("Ingredient")
class TestIngredient:
    @allure.title("Проверка цены ингредиента")
    def test_get_price_returns_correct_ingredient_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "space sauce", 80)

        assert ingredient.get_price() == 80

    @allure.title("Проверка названия ингредиента")
    def test_get_name_returns_correct_ingredient_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "beef cutlet", 3000)

        assert ingredient.get_name() == "beef cutlet"

    @allure.title("Проверка типа ингредиента")
    @pytest.mark.parametrize("ingredient_type", [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_get_type_returns_correct_ingredient_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, "test ingredient", 150)

        assert ingredient.get_type() == ingredient_type
