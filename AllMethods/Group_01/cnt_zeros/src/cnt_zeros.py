def cnt_zeros(elements):
    if not isinstance(elements, list):
        raise TypeError("Input must be a list")
        
    cnt = 0
    for elem in elements:
        if elem == 0:
            cnt += 1

    return cnt
