'''
receive file to parse
print file to terminal for testing
multiply measurements correctly
convert measurement units correctly
'''
from recipe import get_ingredients, standardize_units, convert_to_tsp, convert_to_nearest, convert, recipe_multi

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
    print("test_recipe_parsing_1 passed")

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
        ['garlic', 1, 'tablespoon', 'minced'], 
        ['flour', 2, 'tbsp'], 
        ['heavy-cream', 1.5, 'cup']]
    assert get_ingredients(recipe) == expected
    print("test_recipe_parsing_2 passed")

def test_standardize_units_1():
    '''
    Test the standardize_units function with a simple list of ingredients with a mix of abbreviations and full words.
    The recipe is a JSON string with three ingredients: salted butter, 1 tablespoon of garlic, 2 tablespoons of flour, 
    and 1.5 cups of heavy cream.
    The expected output is a list of three lists, each containing the name, amount, and if they have them, unit, and 
    note of an ingredient.
    '''
    unit = ["gallons", "quarts", "pints", "cups", "tablespoons", "teaspoons"]
    expected = ["gal", "qt", "pt", "cup", "tbsp", "tsp"]
    for x in range(len(unit)):
        assert standardize_units(unit[x]) == expected[x]
    print("test_standardize_units_1 passed")

def test_standardize_units_2():
    unit = ["gallon", "qt", "pint", "cup", "tablespoon", "tsp"]
    expected = ["gal", "qt", "pt", "cup", "tbsp", "tsp"]
    for x in range(len(unit)):
        assert standardize_units(unit[x]) == expected[x]
    print("test_standardize_units_2 passed")

def test_convert_to_tsp_1():
    unit_type = "tbsp"
    amount = 8
    expected = 24
    assert convert_to_tsp(unit_type, amount) == expected
    print("test_convert_to_tsp_1 passed")

def test_convert_to_tsp_2():
    unit_type = "tsp"
    amount = 8
    expected = 8
    assert convert_to_tsp(unit_type, amount) == expected
    print("test_convert_to_tsp_2 passed")

def test_convert_to_tsp_3():
    unit_type = "cup"
    amount = 8
    expected = 384
    assert convert_to_tsp(unit_type, amount) == expected
    print("test_convert_to_tsp_3 passed")

def convert_to_tsp_4():
    unit_type = "gallon"
    amount = 2
    expected = 1536
    assert convert_to_tsp(unit_type, amount) == expected

def test_convert_to_nearest_1():
    amount = 24
    expected = [0, 0, 0.5, 0, 0]
    assert convert_to_nearest(amount) == expected
    print("test_convert_to_nearest_1 passed")

def test_convert_to_nearest_2():
    amount = 25
    expected = [0, 0, 0.5, 0, 1]
    assert convert_to_nearest(amount) == expected
    print("test_convert_to_nearest_2 passed")

def test_convert_to_nearest_3():
    amount = 768
    expected = [1, 0, 0, 0, 0]
    assert convert_to_nearest(amount) == expected
    print("test_convert_to_nearest_3 passed")

def test_convert_to_nearest_4():
    amount = 28
    expected = [0, 0, 0.5, 1, 1]
    assert convert_to_nearest(amount) == expected
    print("test_convert_to_nearest_4 passed")

def test_convert_1():
    unit_type = "tsp"
    amount = 2
    expected = [0, 0, 0, 0, 2]
    assert convert(unit_type, amount) == expected
    print("test_convert_1 passed")

def test_convert_2():
    unit_type = "tsp"
    amount = 4
    expected = [0, 0, 0, 1, 1]
    assert convert(unit_type, amount) == expected
    print("test_convert_2 passed")

def test_convert_3():
    unit_type = "tbsp"
    amount = 12
    expected = [0, 0, 0.75, 0, 0]
    assert convert(unit_type, amount) == expected
    print("test_convert_3 passed")

def test_convert_4():
    unit_type = "tbsp"
    amount = 7
    expected = [0, 0, 0.25, 3, 0]
    assert convert(unit_type, amount) == expected
    print("test_convert_4 passed")

def test_recipe_multi_1():
    PATH = 'test.json'
    expected = [['egg', 1], ['flour', 2, 'tablespoons'], ['butter', 1, 'stick', 'softened']]
    assert recipe_multi(PATH) == expected
    print("test_recipe_multi_1 passed")

def test_recipe_multi_1_1():
    PATH = 'test.json'
    Multiplier = 3
    expected = [['egg', 3], ['flour', 2, 'tbsp', 0.25, 'c'], ['butter', 3, 'stick', 'softened']]
    assert recipe_multi(PATH, Multiplier) == expected

def test_recipe_multi_2():
    PATH = 'test2.json'
    expected = [['salted-butter', 2, 'tbsp', 0.25, 'c'], ['garlic', 1, 'tbsp', 'minced'], ['flour', 2, 'tbsp'], ['heavy-cream', 1.5, 'c']]
    assert recipe_multi(PATH) == expected
    print("test_recipe_multi_2 passed")

def test_recipe_multi_3():
    PATH = 'cake-mix-cookies-recipe.json'
    expected = [['cake-mix', 1, 'box'], ['water', 1, 'tbs'], ['egg', 1], ['butter', 8, 'tbsp', 'softened'], ['chocolate-chips', 1, 'c'] ]
    assert recipe_multi(PATH) == expected
    print("test_recipe_multi_3 passed")
def test_recipe_multi_4():
    PATH = "alfredo-recipe.json"
    expected = [['salted-butter', 2, 'tablespoons', 0.25, 'cups'], ['garlic', 1, 'tbsp', 'minced'], ['flour', 2, 'tbsp'], ['heavy-cream', 1.5, 'c'], ['whole-milk', 1.5, 'c', '1% or 2% can be used if needed'], ['parmesan-cheese', 0.5, 'c', 'grated and at room temperature'], ['romano-cheese', 0.5, 'c', 'grated and at room temperature'], ['salt-and-pepper', 'to taste'], ['fettuccine-pasta', 1, 'lb'], ['parsley', 'to garnish']]
    assert recipe_multi(PATH) == expected
    print("test_recipe_multi_4 passed")



def run_tests():
    test_recipe_parsing_1()
    test_recipe_parsing_2()
    test_standardize_units_1()
    test_standardize_units_2()
    test_convert_to_tsp_1()
    test_convert_to_tsp_2()
    test_convert_to_tsp_3()
    test_convert_to_nearest_1()
    test_convert_to_nearest_2()
    test_convert_to_nearest_3()
    test_convert_to_nearest_4()
    test_convert_1()
    test_convert_2()
    test_convert_3()
    test_convert_4()


run_tests()