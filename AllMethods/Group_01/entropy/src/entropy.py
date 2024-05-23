import math

def entropy(k):
    total = sum(k)
    if total == 0:
        raise ValueError("The sum of the elements should not be zero.")
    
    h = 0
    for value in k:
        if value != 0:
            p_i = value / total
            h += p_i * math.log(p_i)
    
    return -h
