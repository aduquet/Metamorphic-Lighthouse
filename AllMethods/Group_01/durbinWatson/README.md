### README for Durbin-Watson Function

#### Function Description:
The `durbinWatson` function computes the Durbin-Watson statistic for a given dataset. The Durbin-Watson statistic is a number that tests for autocorrelation in the residuals from a statistical regression analysis. The value of this statistic can vary between 0 and 4. A value of 2 indicates no autocorrelation, while values approaching 0 suggest positive autocorrelation and values towards 4 suggest negative autocorrelation.

#### Parameters:
- `data`: A list of numbers, typically representing residuals from a regression model. The list should not be empty.

#### Returns:
- The Durbin-Watson statistic as a float.

#### Raises:
- `ValueError`: If the input `data` list is empty.

#### Function Logic:
1. **Input Validation**: 
   - Checks if the `data` list is empty. If so, raises a `ValueError`.
2. **Initializations**:
   - Initializes `run` (accumulates the sum of squared differences between consecutive data points) and `run_sq` (accumulates the sum of squared data points).
3. **Calculate Statistic**:
   - Iterates through the dataset starting from the second element.
   - For each element, calculates the difference between it and its predecessor, squares this difference, and adds it to `run`.
   - Also adds the square of each data point to `run_sq`.
4. **Compute and Return Durbin-Watson Statistic**:
   - Divides `run` by `run_sq` to obtain the Durbin-Watson statistic.
   - Returns this statistic.

#### Usage Example:
```python
residuals = [1.3, 2.1, 1.8, 2.5, 2.0]
dw_statistic = durbinWatson(residuals)
print(dw_statistic)
# Output will be the Durbin-Watson statistic for the provided residuals
```

#### Note:
The Durbin-Watson statistic is widely used in the field of econometrics and other disciplines that rely on regression analysis. It is an essential tool for diagnosing whether the assumptions of independence and homoscedasticity (constant variance) are met in the residuals of a regression model. This function assumes a basic understanding of regression analysis and the concept of autocorrelation.