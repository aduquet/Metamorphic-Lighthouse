```markdown
# Testing `harmonicMean` Function

This repository provides a suite of tests for the `harmonicMean` function, which calculates the harmonic mean of a given list of positive numbers.

## Tests Explanation

- `test_positive_numbers`: Tests the harmonic mean of a typical list of positive numbers.
- `test_single_number`: Tests the harmonic mean of a list containing a single number.
- `test_empty_list`: Tests if a ValueError is raised for an empty list.
- `test_negative_numbers`: Tests if a ValueError is raised for a list containing negative numbers.
- `test_zero_in_list`: Tests if a ValueError is raised for a list containing zero.
- `test_non_list_input`: Tests if a TypeError is raised for a non-list input.

## Running the Tests

You can run the tests in different ways:

1. **Using unittest from Command Line**:
   ```bash
   python3 -m unittest test_harmonicMean.py
   ```

2. **Running the Script Directly**:
   ```bash
   python3 test_harmonicMean.py
   ```

For a more verbose output detailing each test method and its result, add `-v` to the command:
   ```bash
   python3 -m unittest -v test_harmonicMean.py
   ```