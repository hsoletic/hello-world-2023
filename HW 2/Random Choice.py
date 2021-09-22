import random

(Rug) = {"brand": ["Zarin Rugs", "Lowes", "Home Depot"] ,
"area": ["kitchen", "living room", "bedroom"],
"size": ["2 x 3", "5 x 8", "7 x 9"],
"color": ["yellow", "pink", "black"],
"pattern": ["circle", "wave", "square"],
"knot-count": ["200", "260", "330"],
"washable": ["True", "False"]}

print("Here is your Rug option:")
print("Brand: "+random.choice(Rug ["brand"]))
print("Area: "+random.choice(Rug ["area"]))
print("Size: "+random.choice(Rug ["size"]))
print("Pattern: "+random.choice(Rug ["pattern"]))
print("Color: "+random.choice(Rug ["color"]))
print("Knot-count: "+random.choice(Rug ["knot-count"]))
print("Washable: "+random.choice(Rug ["washable"]))

#[random.choice("brand")]
#print(Rug) [random.choice("brand")]

#number_list = [111, 222, 333, 444, 555]
# random item from list
#print(random.choice(number_list))