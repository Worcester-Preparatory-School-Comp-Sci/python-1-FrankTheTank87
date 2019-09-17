years = float(input("How many years has it been? "))
def births(x):
    x = years*365*24*60*60
    y = x/7
    return(y)
def deaths(x):
    x = years*365*24*60*60
    y = x/13
    return(y)
def immigrants(x):
    x = years*365*24*60*60
    y = x/35
    return(y)
def new_population(x):
    x = births(years) + immigrants(years) - deaths(years) + 307357870
    return(x)
print("The population is now approximately", new_population(years),"people.")
