### README for Variance Calculation Function

#### Function Description:
The `variance` function calculates the variance of a list of numerical values. Variance is a measure of the spread or dispersion of data points around the mean. It is widely used in statistics, data analysis, and machine learning to understand the variability within a dataset.

#### Parameters:
- `data`: A list of numerical elements (integers or floats).

#### Returns:
- The variance of the data, a non-negative numeric value.

#### Raises:
- `TypeError`: If the input is not a list or if the list contains non-numeric elements.
- `ValueError`: If the list is empty.

#### Function Logic:
1. **Input Validation**: 
   - Checks if the input `data` is a list and contains only numeric elements. If not, raises the appropriate `TypeError`.
   - Verifies that the list is not empty. If it is empty, raises a `ValueError` because variance cannot be calculated for an empty dataset.
2. **Mean Calculation**:
   - Calculates the mean (average) of the data by summing all elements and dividing by the number of elements.
3. **Variance Calculation**:
   - Computes the variance by iterating through each element in the list.
   - For each element, subtracts the mean, squares the result, and adds it to a running sum.
   - Divides the sum by the number of elements to obtain the variance.
4. **Return Variance**: Returns the computed variance of the data.

#### Usage Example:
```python
data = [2, 4, 6, 8, 10]
result = variance(data)
print(result)
# Output: 8.0
```