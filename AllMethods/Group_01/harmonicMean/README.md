### README for Harmonic Mean Function

#### Function Description:
The `harmonicMean` function calculates the harmonic mean of a list of numbers. The harmonic mean is a kind of average, typically used when the numbers are defined in relation to some unit (e.g., speed, density). It is especially useful in situations where the average of rates is needed. This function is relevant in fields like finance, physics, and various kinds of statistical reporting.

#### Parameters:
- `data`: A list of positive numerical elements (integers or floats).

#### Returns:
- The harmonic mean of the list as a float.

#### Raises:
- `ValueError`: If the list is empty or contains non-positive numbers.
- `TypeError`: If any element in the list is not a number.

#### Function Logic:
1. **Input Validation**: 
   - Checks if the list `data` is empty. If so, raises a `ValueError`.
   - Iterates over each element in `data` to ensure they are positive numbers. If any number is non-positive or not numeric, raises the appropriate `ValueError` or `TypeError`.
2. **Sum of Inversions**:
   - Initializes a variable `sum_of_inversions` to 0.
   - Iterates over each element in `data`, adding the reciprocal (1/number) of each element to `sum_of_inversions`.
3. **Harmonic Mean Calculation**:
   - Divides the length of the list by `sum_of_inversions` to compute the harmonic mean.
4. **Return Harmonic Mean**: Returns the calculated harmonic mean.

#### Usage Example:
```python
numbers = [1, 2, 4, 8, 16]
harmonic_mean = harmonicMean(numbers)
print(harmonic_mean)
# Output: approximately 2.769230769230769
```
