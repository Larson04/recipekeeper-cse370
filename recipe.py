import json
import sys
from conversions import convert

#hello there
def recipe_multi(PATH, Multiplier=1):
    if not isinstance(PATH, str): 
        sys.exit("Improper file path argument: " + str((PATH)))
    if not isinstance(Multiplier, (int, float)): 
        sys.exit("Improper multiplier argument: " + str((Multiplier)))
    
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
                if isinstance(unit, int):
                    break
                if sum(1 for x in unit if x != 0) >= 2:
                    if not unit[3] + unit[4] == 0:
                        i[2] = "teaspoons"
                        i[1] = unit[4] + unit[3] * 3
                    #else do this and turn into cups
                    else:
                        i[2] = "cups"
                        i[1] = (unit[0] * 16) + (unit[1] * 2) + unit[2]
                else:
                    for x in range(5):
                        if unit[x] != 0:
                            if x == 0:
                                i[2] = "gallons"
                                i[1] = unit[x]
                            if x == 1:
                                i[2] = "quarts"
                                i[1] = unit[x]
                            if x == 2:
                                i[2] = "cups"
                                i[1] = unit[x]
                            if x == 3:
                                i[2] = "tablespoons"
                                i[1] = unit[x]
                            if x == 4:
                                i[2] = "teaspoons"
                                i[1] = unit[x]
                            break

    print(ingredients)
    return ingredients

# recipe_multi("alfredo-recipe.json", 3)

recipe_multi("alfredo-recipe.json", 4)