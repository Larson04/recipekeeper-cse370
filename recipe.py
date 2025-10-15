import json
import sys
from conversions import convert

def get_ingredients(PATH):
    if not isinstance(PATH, str): 
        sys.exit("Improper file path argument: " + str((PATH)))
    #open le json
    with open(PATH, 'r') as file:
        data = json.load(file)
    #use le json
    ingredients = []
    i = 0
    for name, details in data["ingredients"].items():
        ingredients.append([name])
        if details['amount']:
            ingredients[i].append(details['amount'])
        if details['unit']:  # only add if it's not an empty string
            ingredients[i].append(details['unit'])
        if details['note']:  # only add if it's not an empty string
            ingredients[i].append(details['note'])
        i += 1
    file.close()
    return ingredients


def recipe_multi(PATH, Multiplier = 1):
    ingredients = get_ingredients(PATH)
    if not isinstance(Multiplier, (int, float)): 
        sys.exit("Improper multiplier argument: " + str((Multiplier)))
    #items have been parsed
    #list format: [[ingredient, quantity, unit, note], [repeat previous]]
    #print(ingredients) #debug line
    for i in ingredients:
        if isinstance(Multiplier, (int, float)):
            if isinstance(i[1], (int, float)):
                i[1] = i[1] * Multiplier
        if len(i) >= 3:
            if isinstance(i[2], (str)) and isinstance(i[1], (int, float)):
                unit = convert(i[2], i[1])
                #print(unit)
                if isinstance(unit, int):
                    break
                if sum(1 for x in unit if x != 0) >= 2:
                    i.pop(1)
                    i.pop(1)
                    print(i)
                    for x in range(5):
                        if unit[x] != 0:
                            if x == 0:
                                i.insert(1, unit[x])
                                i.insert(2, "gallons")
                            if x == 1:
                                i.insert(1, unit[x])
                                i.insert(2, "quarts")
                            if x == 2:
                                i.insert(1, unit[x])
                                i.insert(2, "cups")
                            if x == 3:
                                i.insert(1, unit[x])
                                i.insert(2, "tablespoons")
                            if x == 4:
                                i.insert(1, unit[x])
                                i.insert(2, "teaspoons")
    print(ingredients)
    return ingredients

# recipe_multi("alfredo-recipe.json", 3)

recipe_multi("alfredo-recipe.json", 7)