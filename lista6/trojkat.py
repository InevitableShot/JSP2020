def circuit(a,b,c):
    return a+b+c

def surface_area(a,b,c):
    from math import sqrt
    p = (a+b+c)/2
    return sqrt(p*(p-a)*(p-b)*(p-c))

def triangle_type(a,b,c):
    if a == b == c:
        return "Jest to trójkąt równoboczny"
    elif a == b or a == c or b == c:
        return "Jest to trójkąt równoramienny"
    else:
        return "Jest to trójkąt różnoboczny"

def triangle_angle(a,b,c):
    sides = sorted((a,b,c))
    if sides[2]**2 > sides[0]**2 + sides[1]**2:
        return "Jest to trójkąt rozwartokątny"
    elif sides[2]**2 == sides[0]**2 + sides[1]**2:
        return "Jest to trójkąt prostokątny"
    elif sides[2]**2 < sides[0]**2 + sides[1]**2:
        return "Jest to trójkąt ostrokątny"