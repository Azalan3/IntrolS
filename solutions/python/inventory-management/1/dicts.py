def create_inventory(items):
    inventory = {}
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory

print (create_inventory(["coal", "wood", "wood", "diamond", "diamond", "diamond"]))

def add_items(inventory, items):
    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory


print (add_items({"coal":1}, ["wood", "iron", "coal", "wood"]))

def decrement_items(inventory, items):

    for item in items:
        if item in inventory and inventory[item] > 0:
            inventory[item] -= 1
    return inventory



print (decrement_items({"coal":3, "diamond":1, "iron":5}, ["diamond", "coal", "iron", "iron"]))
print (decrement_items({"coal":2, "wood":1, "diamond":2}, ["coal", "coal", "wood", "wood", "diamond"]))

def remove_item(inventory, item):
    
        if item in inventory:
            del inventory[item]
        return inventory

print (remove_item({"coal":2, "wood":1, "diamond":2}, "coal"))
print (remove_item({"coal":2, "wood":1, "diamond":2}, "gold"))

def list_inventory(inventory):
    inventory_list = []
    for item in inventory:
        if inventory[item] > 0:
            inventory_list.append((item, inventory[item]))
    return inventory_list

print (list_inventory({"coal":7, "wood":11, "diamond":2, "iron":7, "silver":0}))
