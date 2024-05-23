def harmonicMean(data):
    if not data:  # Check if the list is empty
        raise ValueError("List must not be empty.")
    
    sum_of_inversions = 0
    for number in data:
        if number <= 0:  # Harmonic mean is undefined for non-positive numbers
            raise ValueError("Cannot calculate harmonic mean with non-positive numbers.")
        if not isinstance(number, (int, float)):  # Check for non-numeric values
            raise TypeError("All list elements must be numeric.")
        
        sum_of_inversions += 1 / number

    return len(data) / sum_of_inversions