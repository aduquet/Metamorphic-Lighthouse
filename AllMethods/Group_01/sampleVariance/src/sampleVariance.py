
def sampleVariance(data):
    if not isinstance(data, list):
        raise TypeError("Input should be a list of numbers.")
    
    if not all(isinstance(i, (int, float)) for i in data):
        raise ValueError("List should contain only numbers.")
    
    size = len(data)
    if size < 2:
        raise ValueError("Sample size should be greater than 1 for variance calculation.")
    
    mean = sum(data) / size
    variance_sum = sum((x - mean) ** 2 for x in data)
    
    return variance_sum / (size - 1)
