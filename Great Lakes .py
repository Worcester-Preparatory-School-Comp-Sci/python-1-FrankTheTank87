#Frank Carter, 9-16-19
water = float(input("How many milliliters of water are in the Great Lakes? "))
usa = float(input("What is the surface area in centimeters of the 48 contiguous US states? "))
def depth(x):
    x = water/usa
    return(x)
print("If all the water in the Great Lakes covered the USA, the water would be ",depth(water)," centimeters deep.")


#typically, you would not want your user research and put in these values which are generally constant
