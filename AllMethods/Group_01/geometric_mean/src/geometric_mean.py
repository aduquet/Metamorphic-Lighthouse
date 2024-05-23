import math

def geometric_mean(numbers):
    # Check if the input is a list
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of numbers.")
    
    # Check if the list is empty
    if len(numbers) == 0:
        raise ValueError("List must not be empty.")

    # Initialize the product variable
    product = 1
    
    for i in numbers:
        # Check if the element is numeric
        if not isinstance(i, (int, float)):
            raise TypeError("All list elements must be numeric.")
        
        # Check for non-positive values
        if i <= 0:
            raise ValueError("Numbers must be positive.")
        
        product *= i
    
    # Calculate the geometric mean
    return math.exp(math.log(product) / len(numbers))
