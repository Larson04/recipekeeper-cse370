'''
receive file to parse
print file to terminal for testing
multiply measurements correctly
convert measurement units correctly
'''
from recipe import recipe_multi

def test_recipe_parsing_1():
    '''
    Test the recipe_multi function with a simple list of ingredients.
    The recipe is a JSON string with three ingredients: an egg, 2 tablespoons of flour, and 1 stick of butter.
    The expected output is a list of three lists, each containing the name, amount, unit, and note of an ingredient.
    '''
    recipe = {"ingredients": {
    "egg": {"amount": 1, "unit": " ", "note": " "}, 
    "flour": {"amount": 2, "unit": "tablespoons", "note": " "}, 
    "butter": {"amount": 1, "unit": "stick", "note": "softened"}
    }
    }
    expected = [['egg', 1, ' ', ' '], ['flour', 2, 'tablespoons', ' '], ['butter', 1, 'stick', 'softened']]
    assert recipe_multi(recipe) == expected
    print("test_recipe_multi_1 passed")

def test_recipe_parsing_2():
    '''Test '''
    recipe = "test.json"
    expected = [['salted-butter', 12, 'tbsp', ''], 
                ['garlic', 2, 'tbsp', 'minced'], 
                ['flour', 4, 'tbsp', ''], 
                ['heavy-cream', 3, 'c', '']]
    assert recipe_multi(recipe, 2) == expected
    print("test_recipe_multi_2 passed")


def run_tests():
    test_recipe_parsing_1()
    test_recipe_parsing_2()


run_tests()