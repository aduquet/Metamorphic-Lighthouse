def find_max(a):
    if not a:
        raise ValueError("List cannot be empty")
    
    max_val = a[0]
    for num in a:
        if num > max_val:
            max_val = num

    return max_val
