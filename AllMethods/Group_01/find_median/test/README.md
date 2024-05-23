# Testing `find_median` Function

This repository provides a suite of tests for the `find_median` function, which calculates the median of a given list.

## Tests Explanation

- `test_median_empty_list`: Tests finding the median of an empty list and expects a ValueError.
- `test_median_integer_list_odd`: Tests finding the median in a list of odd-numbered integers.
- `test_median_integer_list_even`: Tests finding the median in a list of even-numbered integers.
- `test_median_float_list_odd`: Tests finding the median in a list of odd-numbered floating-point values.
- `test_median_float_list_even`: Tests finding the median in a list of even-numbered floating-point values.
- `test_median_mixed_list`: Tests finding the median in a mixed list containing integers and floating-point numbers and expects a successful result.
- `test_invalid_input_string`: Tests the median calculation for a single string value and expects a ValueError.
- `test_invalid_input_mixed_list`: Tests the median calculation for a list containing a mix of numbers and strings and expects a ValueError.

## Running the Tests

You can run the tests in different ways:

1. **Using unittest from Command Line**:
   ```bash
   python3 -m unittest test_find_median.py
   ```

2. **Running the Script Directly**:
   ```bash
   python3 test_find_median.py
   ```

For a more verbose output detailing each test method and its result, add `-v` to the command:
   ```bash
   python3 -m unittest -v test_find_median.py
   ```