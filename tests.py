'''
receive file to parse
print file to terminal for testing
multiply measurements correctly
convert measurement units correctly
'''
from recipe import recipe_multi

def test_recipe_multi_1():
    '''
    Test the recipe_multi function with a simple list of ingredients.
    The recipe is a JSON string with three ingredients: an egg, 2 tablespoons of flour, and 1 stick of butter.
    The expected output is a list of three lists, each containing the name, amount, unit, and note of an ingredient.
    '''
    recipe = 'test.json'
    expected = [['egg', 1, ' ', ' '], ['flour', 2, 'tablespoons', ' '], ['butter', 1, 'stick', 'softened']]
    assert recipe_multi(recipe) == expected
    print("test_recipe_multi_1 passed")

def test_recipe_multi_2():
    '''Test '''

def run_tests():
    test_recipe_multi_1()


run_tests()