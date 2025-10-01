import json
import sys
from conversions import convert

#hello there
def recipe_multi(PATH, Multiplier):
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
    #items have been parsed
    #list format: [[ingredient, quantity, unit, note], [repeat previous]]
    #print(ingredients) #debug line
    for i in ingredients:
        #print(i)
        if isinstance(Multiplier, (int, float)):
            i[1] = i[1] * Multiplier
        #convert(i[2], i[1])
    print(ingredients)

recipe_multi("alfredo-recipe.json", 3)