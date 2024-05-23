### README for Max Function

#### Function Description:
The `max` function is designed to find the maximum value in a given list of numbers. This function iterates through each element of the list, comparing each element with the current maximum value, and updating the maximum value as needed. It is an essential function in data analysis, algorithms, and general programming tasks where determining the largest element in a collection of data is required.

#### Parameters:
- `data`: A list of numerical elements. The elements can be integers or floats.

#### Returns:
- The maximum value found in the list.

#### Raises:
- `ValueError`: If the list is empty.
- `TypeError`: If any element in the list is not a number.

#### Function Logic:
1. **Input Validation**: 
   - Checks if the list `data` is empty. If so, raises a `ValueError`, as the maximum value cannot be determined in an empty list.
   - Checks if all elements in the list are numeric. If any element is not numeric, raises a `TypeError`.
2. **Finding Maximum Value**:
   - Initializes `maximum` with the first element of the list.
   - Iterates over each element in the list.
   - Compares each element with `maximum`. If an element is greater than `maximum`, updates `maximum` with this element.
3. **Return Maximum Value**: Returns `maximum`, which holds the maximum value found in the list.

#### Usage Example:
```python
numbers = [3, 5, 1, 8, 7, 2, 6]
max_number = max(numbers)
print(max_number)
# Output: 8
```

