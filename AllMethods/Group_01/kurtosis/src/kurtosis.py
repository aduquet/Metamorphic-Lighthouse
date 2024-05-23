import numpy as np

def kurtosis(data):
    if not isinstance(data, list):
        raise TypeError("Data must be a list.")
    if not data:
        raise ValueError("Data list is empty.")
    if not all(isinstance(x, (int, float)) for x in data):
        raise TypeError("All elements in the data list must be numeric.")
    if len(data) < 4:
        raise ValueError("At least four data points are required to calculate kurtosis.")

    data_array = np.array(data, dtype=np.float64)
    mean = np.mean(data_array)
    standard_deviation = np.std(data_array, ddof=0)
    
    if standard_deviation == 0:
        raise ValueError("Variance of the data is zero.")

    moment4 = np.mean((data_array - mean) ** 4)
    kurt = moment4 / (standard_deviation ** 4)
    excess_kurtosis = kurt - 3

    return excess_kurtosis