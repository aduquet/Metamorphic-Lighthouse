### README for Sample Variance Function

#### Function Description:
The `sampleVariance` function calculates the sample variance of a given dataset. Sample variance is a measure of the dispersion or spread of a set of data points in a sample. It quantifies the degree to which each data point in the set differs from the mean of the data set. This function is particularly valuable in statistical analysis, research, and any field where understanding the variability within a sample is important.

#### Parameters:
- `data`: A list of numerical elements (integers or floats) representing a dataset.

#### Returns:
- The sample variance of the dataset as a float.

#### Raises:
- `TypeError`: If the input is not a list or if the list contains non-numeric elements.
- `ValueError`: If the list contains fewer than two elements, as variance calculation requires at least two data points.

#### Function Logic:
1. **Input Validation**: 
   - Checks if the input `data` is a list and contains only numeric elements. If not, raises the appropriate `TypeError`.
   - Checks if the list has at least two data points, necessary for a valid variance calculation. If not, raises a `ValueError`.
2. **Variance Calculation**:
   - Calculates the mean of the data.
   - Accumulates the squared differences between each data point and the mean.
   - Divides this accumulated sum by the sample size minus one to calculate the sample variance.
3. **Return Sample Variance**: Returns the calculated sample variance.

#### Usage Example:
```python
data = [1, 2, 3, 4, 5]
variance = sampleVariance(data)
print(variance)
# Output: 2.5
```
