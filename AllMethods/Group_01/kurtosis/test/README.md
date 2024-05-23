
```markdown
# Testing `kurtosis` Function

This repository provides a suite of tests for the `kurtosis` function, which computes the kurtosis of a given list of numbers.

## Tests Explanation

- `test_kurtosis_of_integer_list`: Tests the kurtosis of a list of integers.
- `test_kurtosis_of_float_list`: Tests the kurtosis of a list of floating-point numbers.
- `test_kurtosis_of_empty_list`: Tests the kurtosis of an empty list.
- `test_kurtosis_of_non_numerical_list`: Tests the kurtosis of a list containing non-numerical values.
- `test_kurtosis_of_mixed_list`: Tests the kurtosis of a mixed list of numbers and non-numerical values.

## Running the Tests

You can run the tests in different ways:

1. **Using unittest from Command Line**:
   ```bash
   python3 -m unittest test_kurtosis.py
   ```

2. **Running the Script Directly**:
   ```bash
   python3 test_kurtosis.py
   ```

For a more verbose output detailing each test method and its result, add `-v` to the command:
   ```bash
   python3 -m unittest -v test_kurtosis.py
   ```
```
