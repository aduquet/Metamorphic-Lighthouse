
def reverse(a):
    if not isinstance(a, list):
        raise TypeError("Input should be a list")
    
    r = []
    for i in range(len(a) - 1, -1, -1):
        r.append(a[i])
    
    return r
