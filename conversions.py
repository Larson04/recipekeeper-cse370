import math

# returns amount in measurements of [gallons, quarts, cups, tablespoons, teaspoons]
def convert(unit_type, amount):
    new_amount = convert_to_tsp(unit_type, amount)
    final_measurement = convert_to_nearest(new_amount)
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
    return [gal, qt, cup, tbsp, tsp]

print(convert("tsp", 546))