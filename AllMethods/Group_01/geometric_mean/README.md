### README for Geometric Mean Function

#### Function Description:
The `geometric_mean` function calculates the geometric mean of a list of numbers. The geometric mean is a type of mean or average, which indicates the central tendency or typical value of a set of numbers by using the product of their values. This function is particularly useful in situations where the numbers are of different orders of magnitude or when dealing with rates of change, like in financial growth rates, population growth, or in certain scientific contexts.

#### Parameters:
- `numbers`: A list of positive numerical elements (integers or floats).

#### Returns:
- The geometric mean of the list as a float.

#### Raises:
- `TypeError`: If the input is not a list or if any element in the list is not a number.
- `ValueError`: If the list is empty or contains non-positive numbers.

#### Function Logic:
1. **Input Validation**: 
   - Checks if the input `numbers` is a list of numerical values. If not, raises a `TypeError`.
   - Checks if the list is empty, or if any number in the list is non-positive. If so, raises a `ValueError`.
2. **Product Calculation**:
   - Initializes a variable `product` to 1.
   - Iterates over each element in the list, multiplying each element to `product`.
3. **Geometric Mean Calculation**:
   - Uses the logarithm to calculate the geometric mean, avoiding potential issues with large products.
   - Takes the natural logarithm (`math.log`) of `product`, divides it by the number of elements, and then takes the exponential (`math.exp`) of the result.
4. **Return Geometric Mean**: Returns the geometric mean of the list.

#### Usage Example:
```python
numbers = [1, 3, 9, 27, 81]
geo_mean = geometric_mean(numbers)
print(geo_mean)
# Output: 9.0
```

