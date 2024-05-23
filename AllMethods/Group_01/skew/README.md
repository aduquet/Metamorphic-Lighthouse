### README for Skewness Calculation Function

#### Function Description:
The `skew` function calculates the skewness of a given dataset, which is a measure of the asymmetry or lack of symmetry in the distribution of data points. It quantifies whether the data is skewed to the left (negatively skewed) or to the right (positively skewed), or if it is approximately symmetric. Skewness is an essential statistic in data analysis, finance, and various scientific fields.

#### Parameters:
- `data`: A list of numerical elements (integers or floats) representing a dataset.

#### Returns:
- The skewness of the dataset as a float.

#### Raises:
- `TypeError`: If the input is not a list or if the list contains non-numeric elements.
- `ValueError`: If the list contains fewer than three elements, as skewness calculation requires at least three data points.

#### Function Logic:
1. **Input Validation**: 
   - Checks if the input `data` is a list and contains only numeric elements. If not, raises the appropriate `TypeError`.
   - Checks if the list has at least three data points, necessary for a valid skewness calculation. If not, raises a `ValueError`.
2. **Mean and Standard Deviation Calculation**:
   - Calculates the mean of the data.
   - Calculates the variance of the data.
   - Computes the standard deviation from the variance. Checks for a zero standard deviation and raises an error if found, as skewness is undefined in this case.
3. **Skewness Calculation**:
   - Accumulates the cubed differences between each data point and the mean.
   - Divides this accumulated sum by the sample size.
   - Divides the skewness sum by the cubed standard deviation to calculate skewness.
4. **Return Skewness**: Returns the calculated skewness value.

#### Usage Example:
```python
data = [1, 2, 2, 3, 3, 3, 4, 4, 5]
skewness = skew(data)
print(skewness)
# Output: 0.4681095681309035 (approximately)
```

#### Note:
Skewness provides insights into the shape and symmetry of a dataset. A positive skewness indicates a longer right tail, while a negative skewness indicates a longer left tail. A skewness value close to zero suggests approximate symmetry. This function is particularly useful for understanding the distribution of data, especially in fields where the shape of the distribution is critical, such as finance and economics.