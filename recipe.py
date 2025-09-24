import json

#hello there
def recipe_multi(PATH, Multiplier):
    #open le json
    with open('PATH', 'r') as file:
        data = json.load(file)
    #use le json
