#Frank Carter, 9-16-19
gallons = float(input("How many gallons of gasoline are there? "))
def liters(x):
    x = gallons*3.78541
    return(x)
def barrels(x):
    x = gallons/19.5
    return(x)
def co2(x):
    x = gallons*20
    return(x)
def price(x):
    x = gallons*3.35
    return(x)
print("There are", liters(gallons), "liters of gasoline.")
print("It requires", barrels(gallons), "barrels of crude oil.")
print(co2(gallons), "pounds of carbon dioxide will be produced.")
print("It will cost $",price(gallons), "US dollars.")
