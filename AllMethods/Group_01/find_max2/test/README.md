
# Max Consecutive Sum Function Test Suite

This repository contains the implementation and test suite for the `find_max2` function, which returns the maximum sum of two consecutive numbers in a list.

## Function:
```python
def find_max2(a):
    if len(a) < 2:
        raise ValueError("List must contain at least two elements")
    max_sum = a[0] + a[1]
    for i in range(1, len(a) - 1):
        current_sum = a[i] + a[i + 1]
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum
```

## Test Cases:

`test_list_too_small`: Test if the function handles a list with fewer than two elements.
`test_all_positive` Test with a list containing all positive numbers.
`test_all_negative` Test with a list containing all negative numbers.
`test_mixed_positive_negative` Test with a list containing a mix of positive and negative numbers.
`test_with_zero` Test with a list that contains zero.

## Running the Tests

You can run the tests in different ways:

1. **Using unittest from Command Line**:
   ```bash
   python3 -m unittest test_array_copy.py
   ```

2. **Running the Script Directly**:
   ```bash
   python3 test_array_copy.py
   ```

For a more verbose output detailing each test method and its result, add `-v` to the command:
   ```bash
   python3 -m unittest -v test_array_copy.py
   ```