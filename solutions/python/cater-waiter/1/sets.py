from sets_categories_data import (
    VEGAN,
    VEGETARIAN,
    KETO,
    PALEO,
    OMNIVORE,
    ALCOHOLS,
    SPECIAL_INGREDIENTS,
    EXAMPLE_INTERSECTION,
    example_dishes,
)


def clean_ingredients(dish_name, dish_ingredients):

    return (dish_name, set(dish_ingredients))


print(
    clean_ingredients(
        "Punjabi-Style Chole",
        [
            "onions",
            "tomatoes",
            "ginger paste",
            "garlic paste",
            "ginger paste",
            "vegetable oil",
            "bay leaves",
            "cloves",
            "cardamom",
            "cilantro",
            "peppercorns",
            "cumin powder",
            "chickpeas",
            "coriander powder",
            "red chili powder",
            "ground turmeric",
            "garam masala",
            "chickpeas",
            "ginger",
            "cilantro",
        ],
    )
)


def check_drinks(drink_name, drink_ingredients):

    for ingredient in drink_ingredients:
        if ingredient in ALCOHOLS:
            return f"{drink_name} Cocktail"
    return f"{drink_name} Mocktail"


print(
    check_drinks(
        "Honeydew Cucumber",
        [
            "honeydew",
            "coconut water",
            "mint leaves",
            "lime juice",
            "salt",
            "english cucumber",
        ],
    )
)
print(
    check_drinks(
        "Shirley Tonic",
        [
            "cinnamon stick",
            "scotch",
            "whole cloves",
            "ginger",
            "pomegranate juice",
            "sugar",
            "club soda",
        ],
    )
)


def categorize_dish(dish_name, dish_ingredients):

    ingredients_set = set(dish_ingredients)

    if ingredients_set.issubset(VEGAN):
        return f"{dish_name}: VEGAN"
    elif ingredients_set.issubset(VEGETARIAN):
        return f"{dish_name}: VEGETARIAN"
    elif ingredients_set.issubset(PALEO):
        return f"{dish_name}: PALEO"
    elif ingredients_set.issubset(KETO):
        return f"{dish_name}: KETO"
    else:
        return f"{dish_name}: OMNIVORE"


print(
    categorize_dish(
        "Sticky Lemon Tofu",
        {
            "tofu",
            "soy sauce",
            "salt",
            "black pepper",
            "cornstarch",
            "vegetable oil",
            "garlic",
            "ginger",
            "water",
            "vegetable stock",
            "lemon juice",
            "lemon zest",
            "sugar",
        },
    )
)

print(
    categorize_dish(
        "Shrimp Bacon and Crispy Chickpea Tacos with Salsa de Guacamole",
        {
            "shrimp",
            "bacon",
            "avocado",
            "chickpeas",
            "fresh tortillas",
            "sea salt",
            "guajillo chile",
            "slivered almonds",
            "olive oil",
            "butter",
            "black pepper",
            "garlic",
            "onion",
        },
    )
)


def tag_special_ingredients(dish):
    dish_name, dish_ingredients = dish
    special_ingredients_found = set()

    for ingredient in dish_ingredients:
        if ingredient in SPECIAL_INGREDIENTS:
            special_ingredients_found.add(ingredient)

    return (dish_name, special_ingredients_found)


print(
    tag_special_ingredients(
        (
            "Ginger Glazed Tofu Cutlets",
            [
                "tofu",
                "soy sauce",
                "ginger",
                "corn starch",
                "garlic",
                "brown sugar",
                "sesame seeds",
                "lemon juice",
            ],
        )
    )
)
print(
    tag_special_ingredients(
        (
            "Arugula and Roasted Pork Salad",
            [
                "pork tenderloin",
                "arugula",
                "pears",
                "blue cheese",
                "pine nuts",
                "balsamic vinegar",
                "onions",
                "black pepper",
            ],
        )
    )
)


def compile_ingredients(dishes):
    all_ingredients = set()
    for dish in dishes:
        ingredients = dish
        all_ingredients.update(ingredients)
    return all_ingredients


dishes = [
    {
        "tofu",
        "soy sauce",
        "ginger",
        "corn starch",
        "garlic",
        "brown sugar",
        "sesame seeds",
        "lemon juice",
    },
    {
        "pork tenderloin",
        "arugula",
        "pears",
        "blue cheese",
        "pine nuts",
        "balsamic vinegar",
        "onions",
        "black pepper",
    },
    {
        "honeydew",
        "coconut water",
        "mint leaves",
        "lime juice",
        "salt",
        "english cucumber",
    },
]

print(compile_ingredients(dishes))


def separate_appetizers(dishes, appetizers):
    apps = set(appetizers)
    result, seen = [], set()
    for dish in dishes:
        if dish not in apps and dish not in seen:
            result.append(dish)
            seen.add(dish)
    return result                 


dishes = [
    "Avocado Deviled Eggs",
    "Flank Steak with Chimichurri and Asparagus",
    "Kingfish Lettuce Cups",
    "Grilled Flank Steak with Caesar Salad",
    "Vegetarian Khoresh Bademjan",
    "Avocado Deviled Eggs",
    "Barley Risotto",
    "Kingfish Lettuce Cups",
]

appetizers = [
    "Kingfish Lettuce Cups",
    "Avocado Deviled Eggs",
    "Satay Steak Skewers",
    "Dahi Puri with Black Chickpeas",
    "Avocado Deviled Eggs",
    "Asparagus Puffs",
    "Asparagus Puffs",
]


print(separate_appetizers(dishes, appetizers))

def singleton_ingredients(dishes, intersection):


    singleton_ings = set()
    for dish in dishes:
        for ingredient in dish:
            if ingredient not in intersection:
                singleton_ings.add(ingredient)
    return singleton_ings

print (singleton_ingredients(example_dishes, EXAMPLE_INTERSECTION))