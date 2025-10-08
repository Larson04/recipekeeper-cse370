import json
import sys
from conversions import convert
from fractions import Fraction

def recipe_multi(PATH, targets_servings=None):
    if not isinstance(PATH, str):
        sys.exit("Improper file path argument: " + str((PATH)))
    
    with open(PATH, 'r') as file:
        data = json.load(file)
    
    original_servings = data.get("servings", 1)

    if targets_servings is None:
        target_services = original_servings
    
    multiplier = targets_servings / original_servings

    ingredients = []
    i = 0
    for name, details in data["ingredients"].items():
        ingredients.append([name])
        if details['amount']:
            ingredients[i].append(details['amount'] * multiplier)
        if details['unit']:
            ingredients[i].append(details['unit'])
        if details['note']:
            ingredients[i].append(details['note'])
        i += 1
    
    for i in ingredients:
        if len(i) >= 3:
            if isinstance(i[2], str) and isinstance(i[1], (int, float)):
                unit = convert(i[2], i[1])
                if sum(1 for x in unit if x != 0) >= 2:
                    ...
                else:
                    for x in range(5):
                        if unit[x] != 0:
                            if x == 1:
                                i[2] = "gallons"
                                i[1] = unit[x]
                            if x == 2:
                                i[2] = "quarts"
                                i[1] = unit[x]
                            if x == 3:
                                i[2] = "cups"
                                i[1] = unit[x]
                            if x == 4:
                                i[2] = "tablespoons"
                                i[1] = unit[x]
                            if x == 5:
                                i[2] = "teaspoons"
                                i[1] = unit[x]
                            break
    print(f'Scaled Recipe for {targets_servings} servings:')
    print(ingredients)
        
    recipe_multi("recipes/pancakes.json", targets_servings=3)
        


# cups_of_flower = 1 

# targets_cups_f = 3

# cups_needed = Fraction(targets_cups_f/cups_of_flower)

# print(f"Cups of flower: {cups_needed}")
