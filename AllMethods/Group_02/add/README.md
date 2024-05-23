#### Function Description:
The `add` function is designed to add corresponding elements of two arrays of equal length. It iterates over the elements of the input arrays, adding the values at each index, and returns a new array with these sums.

#### Parameters:
- `array1`: A list of integers.
- `array2`: Another list of integers.

#### Returns:
- A list where each element is the sum of the corresponding elements from `array1` and `array2`.

#### Raises:
- `ValueError`: If the lengths of `array1` and `array2` are not equal.

#### Test Suite:
A comprehensive test suite accompanies the function to ensure its correctness in various scenarios. The tests include handling of arrays with the same length, empty arrays, arrays of different lengths, and arrays containing negative numbers.

#### Usage Example:
```python
result = add([1, 2, 3], [4, 5, 6])
# result will be [5, 7, 9]
```
