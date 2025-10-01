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
                convert(i[2], i[1])
    print(ingredients)

recipe_multi("cake-mix-cookies-recipe.json", 4)