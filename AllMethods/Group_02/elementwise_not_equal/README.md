
# README for `elementwise_not_equal` Function

## Overview

The `elementwise_not_equal` function compares two lists element by element and returns a new list containing boolean values. Each boolean value indicates whether the corresponding elements in the two input lists are not equal.

## Function Signature

```python
def elementwise_not_equal(a, b):
    # function implementation
```

## Parameters

- `a` (list): The first list of values.
- `b` (list): The second list of values.

## Returns

- `list`: A list of boolean values. Each value is `True` if the corresponding elements in `a` and `b` are not equal, and `False` otherwise.

## Process

1. Checks that `a` and `b` have the same length, raises a `ValueError` if they do not.
2. Initializes an empty list `r`.
3. Iterates over the elements of `a` and `b`, appending the result of the inequality check (`a[i] != b[i]`) to `r`.
4. Returns the list `r`.

## Test Suite

A test suite for this function would include tests for typical scenarios, such as lists with matching and differing elements, as well as edge cases like empty lists and mismatched list lengths.

## Example Usage

```python
result = elementwise_not_equal([1, 2, 3], [1, 3, 2])
# result will be [False, True, True]
```
