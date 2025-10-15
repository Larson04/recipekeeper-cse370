import math

## returns amount in measurements of [gallons, quarts, cups, tablespoons, teaspoons]
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

# print(convert("tsp", 356))