# Testing `durbinWatson` Function

This repository contains tests for the `durbinWatson` function, which calculates the Durbin-Watson statistic for a given data series.

## Tests Explanation:

- `test_empty_data`: Tests the function with an empty data list.
- `test_single_element_data`: Tests the function with a single element list.
- `test_positive_autocorrelation`: Tests a dataset with positive autocorrelation.
- `test_no_autocorrelation`: Tests a dataset with no significant autocorrelation.
- `test_negative_autocorrelation`: Tests a dataset with negative autocorrelation.

## Running the Tests:

1. **Using unittest from Command Line**:
   ```bash
   python -m unittest test_durbinWatson.py
   ```

2. **Running the Script Directly**:
   ```bash
   python test_durbinWatson.py
   ```

For a more detailed output, add `-v` to the command:
   ```bash
   python -m unittest -v test_durbinWatson.py
   ```