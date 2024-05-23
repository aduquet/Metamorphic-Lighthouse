### README for `dec` Function

#### Overview

The `dec` function is a Python function designed to perform element-wise subtraction between two arrays of equal length. It modifies the first array in place, subtracting each element of the second array from the corresponding element in the first array.

#### Function Signature

```python
def dec(array1, array2):
    # function implementation
```

#### Parameters

- `array1` (list): The first list of numerical values.
- `array2` (list): The second list of numerical values, from which values are subtracted from `array1`.

#### Returns

- `list`: The modified `array1` after element-wise subtraction.

#### Process

1. Checks that `array1` and `array2` have the same length. Raises a `ValueError` if they do not.
2. Performs element-wise subtraction: Each element in `array1` is decreased by the corresponding element in `array2`.
3. Returns the modified `array1`.

#### Test Suite

A test suite is provided to ensure the function's correctness under various scenarios, including normal cases, mismatched array lengths, and empty arrays.

#### Notes

- The function modifies `array1` in place. If you need to keep the original `array1` unchanged, consider using a different approach that does not modify the input arrays.
- Ensure that both `array1` and `array2` are of the same length to avoid runtime errors.

#### Example Usage

```python
result = dec([10, 20, 30], [1, 2, 3])
# result will be [9, 18, 27]
```

This example demonstrates subtracting the elements of the second array from the first array.
