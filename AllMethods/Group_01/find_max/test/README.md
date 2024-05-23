
# Find Max Function Test Suite

This repository contains the implementation and test suite for the `find_max` function, which returns the maximum value from a list of numbers.

## Function:
```python
def find_max(a):
    if not a:
        raise ValueError("List cannot be empty")
    max_val = a[0]
    for num in a:
        if num > max_val:
            max_val = num
    return max_val
```

## Test Cases:

1. Test if the function handles an empty list.
2. Test with a list containing a single element.
3. Test with a list containing all positive numbers.
4. Test with a list containing all negative numbers.
5. Test with a list containing a mix of positive and negative numbers.
6. Test with a list that contains zero.

## Running the Tests

You can run the tests in different ways:

1. **Using unittest from Command Line**:
   ```bash
   python3 -m unittest test_find_max.py
   ```

2. **Running the Script Directly**:
   ```bash
   python3 test_find_max.py
   ```

For a more verbose output detailing each test method and its result, add `-v` to the command:
   ```bash
   python3 -m unittest -v test_find_max.py
   ```