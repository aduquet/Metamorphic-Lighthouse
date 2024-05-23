```markdown
# Testing `geometric_mean` Function

This repository provides a suite of tests for the `geometric_mean` function, which calculates the geometric mean of a given list of positive numbers.

## Tests Explanation

- `test_geometric_mean_positive_numbers`: Tests the geometric mean of a list of positive numbers.
- `test_geometric_mean_single_number`: Tests the geometric mean of a list with a single number.
- `test_empty_list`: Tests the function with an empty list, expecting a ValueError.
- `test_non_numeric_list`: Tests the function with a non-numeric list, expecting a ValueError.
- `test_non_positive_numeric_list`: Tests the function with non-positive numbers, expecting a ValueError.
- `test_invalid_input`: Tests the function with an invalid input, expecting a TypeError.

## Running the Tests

You can run the tests in different ways:

1. **Using unittest from Command Line**:
   ```bash
   python3 -m unittest test_geometric_mean.py
   ```

2. **Running the Script Directly**:
   ```bash
   python3 test_geometric_mean.py
   ```

For a more verbose output detailing each test method and its result, add `-v` to the command:
   ```bash
   python3 -m unittest -v test_geometric_mean.py
   ```
