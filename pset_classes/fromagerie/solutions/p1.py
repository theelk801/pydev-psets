"""
Fromagerie I - Create Inventory
"""

# For the problems in this set, imagine you own a fromagerie (a cheese shop). Write and call function called "create_inventory". Use the list of cheeses below. For each cheese, the function should generate variables for SKU, stock, retail_price, and wholesale_price. (Make sure retail_price > wholesale_price!) Store this info for each cheese in a newly created dict called "inventory" and return that dict from the function.

# *NOTES* To make life easier...
# Use the SKU format 'DRY' followed by 4 digits. The whole thing should be a string.
# The prices can be integers to avoid rounding decimals.

import random

def create_inventory(products):
  inventory = {}
  for i in products:
    num = str(random.randint(1000,10000))
    stock = int(random.randint(0,101))
    sku = 'DRY' + num
    #i.insert(0, sku)

    retail = int(random.randint(9, 18))
    wholesale = int(random.randint(2, 9))
    k = [sku, stock, retail, wholesale]
    
    inventory.update({i: [sku, stock, retail, wholesale]})
  return inventory

cheese_types = [
'brie',
'feta',
'cheddar',
'mozzarella',
'ricotta',
'provolone',
'gruyere',
'pecorino romano',
'parmigiano reggiano',
'gorgonzola',
'pepper jack',
'gouda',
'asiago',
'mascarpone',
'cotija',
'manchego'
]

cheese_inventory = create_inventory(cheese_types)
