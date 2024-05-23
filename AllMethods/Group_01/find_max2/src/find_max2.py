def find_max2(a):
    
    if len(a) < 2:
        raise ValueError("List must contain at least two elements")

    max_sum = a[0] + a[1]
    for i in range(1, len(a) - 1):
        current_sum = a[i] + a[i + 1]
        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum
