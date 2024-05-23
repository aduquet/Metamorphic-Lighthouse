import math

def safeNorm(v):
    if not isinstance(v, list):
        raise TypeError("Input should be a list of numbers.")
    
    if len(v) == 0:
        raise ValueError("List should not be empty")
    
    if not all(isinstance(i, (int, float)) for i in v):
        raise ValueError("List should contain only numbers.")
    
    rdwarf = 3.834e-20
    rgiant = 1.304e+19
    s1 = s2 = s3 = x1max = x3max = 0
    floatn = len(v)
    agiant = rgiant / floatn

    for i in v:
        xabs = abs(i)
        if xabs < rdwarf or xabs > agiant:
            if xabs > rdwarf:
                if xabs > x1max:
                    r = x1max / xabs
                    s1 = 1 + s1 * r * r
                    x1max = xabs
                else:
                    r = xabs / x1max
                    s1 += r * r
            else:
                if xabs > x3max:
                    r = x3max / xabs
                    s3 = 1 + s3 * r * r
                    x3max = xabs
                else:
                    if xabs != 0:
                        r = xabs / x3max
                        s3 += r * r
        else:
            s2 += xabs * xabs

    norm = 0  # initialize
    if s1 != 0:
        norm = x1max * math.sqrt(s1 + s2 / x1max / x1max)
    elif s2 == 0:
        norm = x3max * math.sqrt(s3)
    elif s2 >= x3max:
        norm = math.sqrt(s2 * (1 + x3max / s2 * (x3max * s3)))
    else:
        norm = math.sqrt(x3max * (s2 / x3max + x3max * s3))

    return norm
