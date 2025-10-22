'''
receive file to parse
print file to terminal for testing
multiply measurements correctly
convert measurement units correctly
'''
from recipe import get_ingredients, standardize_units

def test_recipe_parsing_1():
    '''
    Test the get_ingredients function with a simple list of ingredients.
    The recipe is a JSON string with three ingredients: an egg, 2 tablespoons of flour, and 1 stick of butter.
    The expected output is a list of three lists, each containing the name, amount, and if they have them, unit, and 
    note of an ingredient.
    '''
    recipe = "test.json"
    expected = [
        ['egg', 1,], 
        ['flour', 2, 'tablespoons'], 
        ['butter', 1, 'stick', 'softened']]
    assert get_ingredients(recipe) == expected
    print("test_recipe_multi_1 passed")

def test_recipe_parsing_2():
    '''Test the get_ingredients function with a simple list of ingredients.
    The recipe is a JSON string with three ingredients: salted butter, 1 tablespoon of garlic, 2 tablespoons of flour, 
    and 1.5 cups of heavy cream.
    The expected output is a list of three lists, each containing the name, amount, and if they have them, unit, and 
    note of an ingredient.
    '''
    recipe = "test2.json"
    expected = [
        ['salted-butter', 6, 'tbsp'], 
        ['garlic', 1, 'tbsp', 'minced'], 
        ['flour', 2, 'tbsp'], 
        ['heavy-cream', 1.5, 'c']]
    assert get_ingredients(recipe) == expected
    print("test_recipe_multi_2 passed")

def test_standardize_units_1():
    '''
    Test the standardize_units function with a simple list of ingredients with a mix of abbreviations and full words.
    The recipe is a JSON string with three ingredients: salted butter, 1 tablespoon of garlic, 2 tablespoons of flour, 
    and 1.5 cups of heavy cream.
    The expected output is a list of three lists, each containing the name, amount, and if they have them, unit, and 
    note of an ingredient.
    '''

def run_tests():
    test_recipe_parsing_1()
    test_recipe_parsing_2()


run_tests()