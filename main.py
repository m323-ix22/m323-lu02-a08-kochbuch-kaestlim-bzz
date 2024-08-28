"""Kochbuch"""
import json


def adjust_recipe(recipe, num_people):
    factor = num_people / recipe["servings"]
    adjusted_ingredients = {ingredient: amount * factor for ingredient, amount in recipe["ingredients"].items()}
    adjusted_recipe1 = {
        "title": recipe["title"],
        "ingredients": adjusted_ingredients,
        "servings": num_people
    }
    return adjusted_recipe1


def load_recipe(json_string):
    return json.loads(json_string)


if __name__ == "__main__":
    recipe_json = ('{"title": "Spaghetti Bolognese", '
                   '"ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, "Minced Meat": 500}, "servings": 4}')
    original_recipe = load_recipe(recipe_json)
    adjusted_recipe = adjust_recipe(original_recipe, 8)
    print(f"Original Recipe: {original_recipe}")
    print(f"Adjusted Recipe: {adjusted_recipe}")
