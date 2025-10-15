import json
import sys
import math 

def convert(unit_type, amount):
    unit_type = standardize_units(unit_type)
    new_amount = convert_to_tsp(unit_type, amount)
    if new_amount == None:
        print("invalid unit type, conversion failed")
        return amount
    final_measurement = convert_to_nearest(new_amount)
    # print(final_measurement)
    return final_measurement


def convert_to_tsp(unit_type, amount):
    match unit_type:
        case "tbsp":
            amount *= 3
        case "cup":
            amount *= 48
        case "pt":
            amount *= 96
        case "qt":
            amount *= 192
        case "gal":
            amount *= 768
        case "tsp":
            pass
        case _:
            amount = None
    return amount

def convert_to_nearest(amount):
    gal = math.floor(amount/768)
    remainder = amount % 768
    qt = math.floor(remainder/192)
    remainder = remainder % 192
    cup = math.floor(remainder/12)/4
    remainder = remainder % 12
    tbsp = math.floor(remainder/3)
    tsp = remainder % 3
    # if (tsp > 0):
    #     tsp += tbsp * 3
    #     tbsp = 0
    return [gal, qt, cup, tbsp, tsp]

## Determines the unit type and formats appropriately
def standardize_units(unit_type):
    if unit_type in "tablespoons" :
            new_unit = "tbsp"
    elif unit_type in "cups":
            new_unit = "cup"
    elif unit_type in "pints":
            new_unit = "pt"
    elif unit_type in "quarts":
            new_unit = "qt"
    elif unit_type in "gallons":
            new_unit = "gal"
    elif unit_type in "teaspoons":
            new_unit = "tsp"
    else:
         new_unit = unit_type
    return new_unit


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