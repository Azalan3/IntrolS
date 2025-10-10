def add_item(current_cart, items_to_add):
    for item in items_to_add:
        if item in current_cart:
            current_cart[item] += 1
        else:
            current_cart[item] = 1
    return current_cart

print (add_item({'Banana': 3, 'Apple': 2, 'Orange': 1},
        ('Apple', 'Apple', 'Orange', 'Apple', 'Banana')))
print (add_item({'Banana': 3, 'Apple': 2, 'Orange': 1},
        ['Banana', 'Orange', 'Blueberries', 'Banana']))

def read_notes(notes):
    cart = {}
    for note in notes:
        if note in cart:
            cart[note] += 1
        else:
            cart[note] = 1
    return cart

print (read_notes(('Banana','Apple', 'Orange')))
print (read_notes(['Blueberries', 'Pear', 'Orange', 'Banana', 'Apple']))

def update_recipes(ideas, recipe_updates):
    updated = ideas.copy()
    for namem, ingredients in recipe_updates:
        updated[namem] = ingredients
    return updated

print (update_recipes(
    {'Banana Bread' : {'Banana': 1, 'Apple': 1, 'Walnuts': 1, 'Flour': 1, 'Eggs': 2, 'Butter': 1},
    'Raspberry Pie' : {'Raspberry': 1, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1}},
    (('Banana Bread', {'Banana': 4,  'Walnuts': 2, 'Flour': 1, 'Butter': 1, 'Milk': 2, 'Eggs': 3}),)
    ))

print (update_recipes(
    {'Banana Bread' : {'Banana': 1, 'Apple': 1, 'Walnuts': 1, 'Flour': 1, 'Eggs': 2, 'Butter': 1},
    'Raspberry Pie' : {'Raspberry': 1, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1},
    'Pasta Primavera': {'Eggs': 1, 'Carrots': 1, 'Spinach': 2, 'Tomatoes': 3, 'Parmesan': 2, 'Milk': 1, 'Onion': 1}},
    [('Raspberry Pie', {'Raspberry': 3, 'Orange': 1, 'Pie Crust': 1, 'Cream Custard': 1, 'Whipped Cream': 2}),
    ('Pasta Primavera', {'Eggs': 1, 'Mixed Veggies': 2, 'Parmesan': 2, 'Milk': 1, 'Spinach': 1, 'Bread Crumbs': 1}),
    ('Blueberry Crumble', {'Blueberries': 2, 'Whipped Creme': 2, 'Granola Topping': 2, 'Yogurt': 3})]
    ))


def sort_entries(cart):
    return sorted(cart.items())
print (sort_entries({'Banana': 3, 'Apple': 2, 'Orange': 1}))

def send_to_store(cart, aisle_mapping):
    fulfillment_cart = {}


    for item, quantity in cart.items():
        aisle, refrigerated = aisle_mapping[item]  
        fulfillment_cart[item] = [quantity, aisle, refrigerated]  

    return dict(sorted(fulfillment_cart.items(), reverse=True))

print (send_to_store({'Banana': 3, 'Apple': 2, 'Orange': 1, 'Milk': 2},
        {'Banana': ['Aisle 5', False], 'Apple': ['Aisle 4', False], 'Orange': ['Aisle 4', False], 'Milk': ['Aisle 2', True]}))

def update_store_inventory(fulfillment_cart, store_inventory):
    for item in fulfillment_cart:
            if item in store_inventory:
                store_inventory[item][0] -= fulfillment_cart[item][0]
            if store_inventory[item][0] <= 0:
                store_inventory[item][0] = 'Out of Stock'
    return store_inventory

print (update_store_inventory({'Orange': [1, 'Aisle 4', False], 'Milk': [2, 'Aisle 2', True], 'Banana': [3, 'Aisle 5', False], 'Apple': [2, 'Aisle 4', False]},
{'Banana': [15, 'Aisle 5', False], 'Apple': [12, 'Aisle 4', False], 'Orange': [1, 'Aisle 4', False], 'Milk': [4, 'Aisle 2', True]}))



