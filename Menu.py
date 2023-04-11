
from pathlib import Path
from pprint import pprint

path = str(Path(__file__).parent.absolute()) + '/menu.txt'
with open(path, 'r', encoding='UTF-8') as fail:        
    cook_book = {}
    for line in fail:
        dish_name = line.strip()
        product_count = int(fail.readline().strip())
        product = []
        for _ in range(product_count):
            ingredient_name, quantity, measure = fail.readline().strip().split('|')
            product.append({
                'ingredient_name' : ingredient_name,
                'quantity' : quantity,
                'measure' : measure
            })
        fail.readline()
        cook_book[dish_name] = product

    pprint(cook_book, sort_dicts=False)

def get_shop_list_by_dishes(dishes, person_count):
    products = {}
    for dish in dishes:
        if dish in cook_book:
            for ingrds in cook_book.get(dish):
                quantity = {}
                if ingrds.get('ingredient_name') in products.keys():
                    products[ingrds.get('ingredient_name')] = quantity
                    quantity['measure'] = ingrds.get('measure')
                    quantity['quantity'] = (int(ingrds.get('quantity')) + int(
                        ingrds.get('quantity'))) * person_count
                else:
                    products[ingrds.get('ingredient_name')] = quantity
                    quantity['measure'] = ingrds.get('measure')
                    quantity['quantity'] = int(
                        ingrds.get('quantity')) * person_count

    return (products)


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))