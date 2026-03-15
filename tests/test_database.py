import allure
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@allure.feature("Database")
class TestDatabase:
    
    @allure.title("Проверка доступных булок")
    def test_available_buns_returns_all_buns(self):
        db = Database()
        buns = db.available_buns()

        assert len(buns) == 3
        assert buns[0].get_name() == "black bun"
        assert buns[1].get_name() == "white bun"
        assert buns[2].get_name() == "red bun"

    @allure.title("Проверка доступных ингредиентов")
    def test_available_ingredients_returns_all_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()

        assert len(ingredients) == 6

        for i in range(3):
            assert ingredients[i].get_type() == INGREDIENT_TYPE_SAUCE

        for i in range(3, 6):
            assert ingredients[i].get_type() == INGREDIENT_TYPE_FILLING
