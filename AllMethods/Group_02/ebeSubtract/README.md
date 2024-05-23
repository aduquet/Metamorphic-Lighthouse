
### README for `ebeSubtract` Function

#### Overview

The `ebeSubtract` function is designed to perform element-by-element subtraction between two lists of the same length. It subtracts each element of the second list `b` from the corresponding element in the first list `a` and returns the result.

#### Function Signature

```python
def ebeSubtract(a, b):
    # function implementation
```

#### Parameters

- `a` (list): The first list of numerical values.
- `b` (list): The second list of numerical values, from which values are subtracted from the corresponding elements in `a`.

#### Returns

- `list`: A new list containing the result of the element-wise subtraction.

#### Process

1. Checks that `a` and `b` have the same length, raises a `ValueError` if they do not.
2. Creates a copy of `a` and performs element-wise subtraction with elements from `b`.
3. Returns the result list.

#### Test Suite

The provided test suite verifies the function's correctness for various scenarios, including valid subtractions, mismatched list lengths, and empty lists.

#### Notes

- The function ensures that both input lists `a` and `b` are of the same length to perform valid EBE subtraction.
- The function does not modify the original lists but returns a new list with the results.

#### Example Usage

```python
result = ebeSubtract([10, 20, 30], [1, 2, 3])
# result will be [9, 18, 27]
```

This example demonstrates subtracting elements of list `b` from list `a` on an element-by-element basis.
