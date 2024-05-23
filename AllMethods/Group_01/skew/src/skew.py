import math

def skew(data):
    if not isinstance(data, list):
        raise TypeError("Input should be a list of numbers.")
    
    if not all(isinstance(i, (int, float)) for i in data):
        raise ValueError("List should contain only numbers.")
    
    size = len(data)
    if size < 3:  # At least three data points are required
        raise ValueError("Sample size should be greater than 2 for skewness calculation.")
    
    mean = sum(data) / size
    variance_sum = sum((x - mean) ** 2 for x in data)
    variance = variance_sum / size
    std_dev = math.sqrt(variance)
    
    if std_dev == 0:
        raise ValueError("Standard deviation is zero, cannot determine skewness.")
    
    skewness_sum = sum((x - mean) ** 3 for x in data)
    skewness_value = skewness_sum / size
    
    return skewness_value / (std_dev ** 3)
