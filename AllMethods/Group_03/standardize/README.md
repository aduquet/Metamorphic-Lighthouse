### README for Standardize Function

#### Function Description:
The `standardize` function is designed to standardize a list of numerical values. Standardization (or Z-score normalization) is the process of rescaling the attributes of a dataset so they have a mean of 0 and a standard deviation of 1. This function calculates the standardized value for each number in the input list, which is useful in statistical analysis and for algorithms in machine learning.

#### Parameters:
- `data`: A list of numbers (integers or floats) to be standardized.

#### Returns:
- A list containing the standardized (Z-score normalized) values of each element from the input list.

#### Raises:
- `TypeError`: If the input is not a list.
- `ValueError`: If the list contains elements other than numbers (integers or floats).
- `ValueError`: If the list is empty, as standardization cannot be performed.
- `ValueError`: If the standard deviation of the list is zero, making standardization impossible.

#### Function Logic:
1. **Input Validation**: 
   - Checks if the input `data` is a list and contains only numerical values. If not, the appropriate `TypeError` or `ValueError` is raised.
2. **Calculation of Mean and Standard Deviation**:
   - Calculates the mean of the data.
   - Calculates the variance and then the standard deviation.
   - Checks if the standard deviation is zero (in which case, every element in the list is the same, and standardization cannot be performed).
3. **Standardization**:
   - Uses list comprehension to calculate the standardized value for each element. This is done by subtracting the mean from each element and dividing the result by the standard deviation.
4. **Return Standardized List**: Returns the new list containing the standardized values.

#### Usage Example:
```python
numbers = [1, 2, 3, 4, 5]
standardized_numbers = standardize(numbers)
print(standardized_numbers)
# Output will be the standardized values of [1, 2, 3, 4, 5]
```

#### Note:
Standardization is a common preprocessing step for many machine learning algorithms. It is crucial when your data has different scales, and you are comparing measurements that have different units. This function assumes a basic understanding of statistics, specifically the concepts of mean, variance, and standard deviation.