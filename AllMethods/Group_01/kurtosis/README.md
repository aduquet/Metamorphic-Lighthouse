### README for Kurtosis Function

#### Function Description:
The `kurtosis` function calculates the kurtosis of a dataset. Kurtosis is a measure of the "tailedness" of the probability distribution of a real-valued random variable. In simpler terms, it provides insights into the shape of the distribution, particularly the sharpness of the peak and the thickness of the tails. This function computes the excess kurtosis, which adjusts the metric so that a normal distribution has a kurtosis of 0.

#### Parameters:
- `data`: A list of numerical elements (integers or floats) representing a dataset.

#### Returns:
- The excess kurtosis of the dataset as a float.

#### Raises:
- `TypeError`: If the input is not a list or if the list contains non-numeric elements.
- `ValueError`: If the list is empty or contains fewer than four elements, or if the variance of the data is zero.

#### Function Logic:
1. **Input Validation**: 
   - Checks if `data` is a list and contains only numeric elements. Raises appropriate errors otherwise.
   - Checks if the list has at least four data points, necessary for a valid kurtosis calculation.
2. **Kurtosis Calculation**:
   - Converts the data list into a NumPy array for efficient computation.
   - Calculates the mean and standard deviation of the data.
   - Computes the fourth moment (the mean of the raised to the fourth power deviations from the mean).
   - Divides the fourth moment by the fourth power of the standard deviation to find kurtosis.
   - Subtracts 3 from the kurtosis value to find the excess kurtosis.
3. **Return Excess Kurtosis**: Returns the calculated excess kurtosis.

#### Usage Example:
```python
data = [1, 2, 2, 3, 3, 3, 4, 4, 5]
excess_kurt = kurtosis(data)
print(excess_kurt)
# Output: Excess kurtosis value for the data set
```

#### Note:
Kurtosis is a critical tool in statistical analysis, especially in the context of understanding the distribution of a dataset. Excess kurtosis is used to understand how the tails of a distribution differ from the tails of a normal distribution. A positive excess kurtosis indicates a distribution with heavy tails, while a negative value suggests light tails. This function relies on NumPy for efficient numerical computations and assumes that the dataset is sufficiently large (at least four points) to provide a meaningful kurtosis value.