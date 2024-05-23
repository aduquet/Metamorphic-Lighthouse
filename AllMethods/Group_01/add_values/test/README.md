# Testing `add_values` Function

## Tests Explanation

- `test_sum_of_integers`: Tests the sum of a list of integers.
- `test_sum_of_floats`: Tests the sum of a list of floating-point numbers.
- `test_sum_of_mixed_numbers`: Tests the sum of a mixed list containing both integers and floats.
- `test_sum_of_empty_list`: Tests the sum of an empty list.
- `test_sum_of_negative_numbers`: Tests the sum of a list containing negative numbers.
- `test_invalid_data_string`: Tests whether the function raises a `TypeError` when given a list of strings.
- `test_invalid_data_mixed`: Tests whether the function raises a `TypeError` when given a mixed list of numbers and strings.

This suite aims to offer a comprehensive test for the `add_values` function. Depending on specific requirements or edge cases, you might need to make adjustments.

## Running the Tests

You can run the tests in three different ways:

1. **Using unittest from Command Line**:
   ```bash
   python3 -m unittest test_add_values.py
   ```

2. **Running the Script Directly**:
   If you've included the `if __name__ == '__main__':` block in your test script, you can run the tests directly:
   ```bash
   python3 -m unittest test_add_values.py
   ```

3. **With Detailed Output**:
   For a more verbose output detailing each test method and its result, use:
   ```bash
   python -m unittest -v python3 -m unittest test_add_values.py
   ```