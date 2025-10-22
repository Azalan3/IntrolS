from sets_categories_data import (
    VEGAN,
    VEGETARIAN,
    KETO,
    PALEO,
    ALCOHOLS,
    SPECIAL_INGREDIENTS,
)

# ---------------- Task 1 ----------------
def clean_ingredients(dish_name, dish_ingredients):
    """Return (dish_name, deduped_ingredient_set)."""
    return (dish_name, set(dish_ingredients))


# ---------------- Task 2 ----------------
def check_drinks(drink_name, drink_ingredients):
    """Return '<name> Cocktail' if any ingredient is alcoholic; else '<name> Mocktail'."""
    for ingredient in drink_ingredients:
        if ingredient in ALCOHOLS:
            return f"{drink_name} Cocktail"
    return f"{drink_name} Mocktail"


# ---------------- Task 3 ----------------
def categorize_dish(dish_name, dish_ingredients):
    """Return '<name>: <CATEGORY>' based on set containment."""
    ingredients_set = set(dish_ingredients)

    if ingredients_set.issubset(VEGAN):
        return f"{dish_name}: VEGAN"
    if ingredients_set.issubset(VEGETARIAN):
        return f"{dish_name}: VEGETARIAN"
    if ingredients_set.issubset(PALEO):
        return f"{dish_name}: PALEO"
    if ingredients_set.issubset(KETO):
        return f"{dish_name}: KETO"
    return f"{dish_name}: OMNIVORE"


# ---------------- Task 4 ----------------
def tag_special_ingredients(dish):
    """Given (dish_name, ingredients), return (dish_name, set_of_special_ingredients)."""
    dish_name, dish_ingredients = dish
    specials = {ing for ing in dish_ingredients if ing in SPECIAL_INGREDIENTS}
    return (dish_name, specials)


# ---------------- Task 5 ----------------
def compile_ingredients(dishes):
    """Given a list of ingredient sets, return the union as a set."""
    all_ingredients = set()
    for ing_set in dishes:
        all_ingredients.update(ing_set)
    return all_ingredients


# ---------------- Task 6 ----------------
def separate_appetizers(dishes, appetizers):
    """
    Return the list of dish names with appetizer names removed (deduped, order-preserving).
    """
    apps = set(appetizers)
    result, seen = [], set()
    for dish in dishes:
        if dish not in apps and dish not in seen:
            result.append(dish)
            seen.add(dish)
    return result


# ---------------- Task 7 ----------------
def singleton_ingredients(dishes, intersections):
    """
    Return a set of ingredients that appear in exactly ONE dish of the category,
    excluding anything present in `intersections` (ingredients that appear in >1 dish).
    """
    counts = {}
    for ing_set in dishes:
        for ing in ing_set:
            counts[ing] = counts.get(ing, 0) + 1

    singles = {ing for ing, c in counts.items() if c == 1}
    return singles - set(intersections)


# ---------------- Optional local tests (avoid Pylint redefined-outer-name) ----------------
if __name__ == "__main__":
    # Task 1 quick check
    print(
        clean_ingredients(
            "Punjabi-Style Chole",
            [
                "onions", "tomatoes", "ginger paste", "garlic paste", "ginger paste",
                "vegetable oil", "bay leaves", "cloves", "cardamom", "cilantro",
                "peppercorns", "cumin powder", "chickpeas", "coriander powder",
                "red chili powder", "ground turmeric", "garam masala", "chickpeas",
                "ginger", "cilantro",
            ],
        )
    )

    # Task 2 quick checks
    print(
        check_drinks(
            "Honeydew Cucumber",
            ["honeydew", "coconut water", "mint leaves", "lime juice", "salt", "english cucumber"],
        )
    )
    print(
        check_drinks(
            "Shirley Tonic",
            ["cinnamon stick", "scotch", "whole cloves", "ginger", "pomegranate juice", "sugar", "club soda"],
        )
    )

    # Task 3 quick checks
    print(
        categorize_dish(
            "Sticky Lemon Tofu",
            {
                "tofu", "soy sauce", "salt", "black pepper", "cornstarch", "vegetable oil", "garlic",
                "ginger", "water", "vegetable stock", "lemon juice", "lemon zest", "sugar",
            },
        )
    )

    print(
        categorize_dish(
            "Shrimp Bacon and Crispy Chickpea Tacos with Salsa de Guacamole",
            {
                "shrimp", "bacon", "avocado", "chickpeas", "fresh tortillas", "sea salt",
                "guajillo chile", "slivered almonds", "olive oil", "butter", "black pepper",
                "garlic", "onion",
            },
        )
    )

    # Task 5 quick check
    sample_dishes_for_union = [
        {"tofu", "soy sauce", "ginger", "corn starch", "garlic", "brown sugar", "sesame seeds", "lemon juice"},
        {"pork tenderloin", "arugula", "pears", "blue cheese", "pine nuts", "balsamic vinegar", "onions", "black pepper"},
        {"honeydew", "coconut water", "mint leaves", "lime juice", "salt", "english cucumber"},
    ]
    print(compile_ingredients(sample_dishes_for_union))

    # Task 6 quick check
    sample_dishes = [
        "Avocado Deviled Eggs",
        "Flank Steak with Chimichurri and Asparagus",
        "Kingfish Lettuce Cups",
        "Grilled Flank Steak with Caesar Salad",
        "Vegetarian Khoresh Bademjan",
        "Avocado Deviled Eggs",
        "Barley Risotto",
        "Kingfish Lettuce Cups",
    ]
    sample_apps = [
        "Kingfish Lettuce Cups",
        "Avocado Deviled Eggs",
        "Satay Steak Skewers",
        "Dahi Puri with Black Chickpeas",
        "Avocado Deviled Eggs",
        "Asparagus Puffs",
        "Asparagus Puffs",
    ]
    print(separate_appetizers(sample_dishes, sample_apps))

    # Task 7 quick check (usa tus propios datos si quieres)
    example_dishes_local = [
        {"tofu", "soy sauce", "garlic"},
        {"mushrooms", "garlic", "olive oil"},
        {"spinach", "lemon"},
    ]
    example_intersections_local = {"tofu", "garlic"}
    print(singleton_ingredients(example_dishes_local, example_intersections_local))
