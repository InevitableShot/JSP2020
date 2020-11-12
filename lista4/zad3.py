import math 
def convert(data, type=True): #True - Rad_to_Deg ; False - Deg_to_Rad
    return math.degrees(data) if type else math.radians(data)
print(convert(1.3))