### README for Find Min Function

#### Function Description:
The `find_min` function is designed to find the minimum value in a given list of numbers. This function iterates through each element of the list, comparing each element with the current minimum value and updating the minimum value as needed. It is a fundamental function in data analysis, algorithms, and general programming tasks where determining the smallest element in a collection of data is necessary.

#### Parameters:
- `data`: A list of numerical elements. The elements can be integers or floats.

#### Returns:
- The minimum value found in the list.

#### Raises:
- `TypeError`: If the input is not a list or if the list contains elements that are not integers or floats.
- `ValueError`: If the list is empty.

#### Function Logic:
1. **Input Validation**: 
   - Checks if the input `data` is a list and contains only numerical elements. If not, raises the appropriate `TypeError`.
   - Checks if the list `data` is empty. If so, raises a `ValueError` since the minimum value cannot be determined in an empty list.
2. **Finding Minimum Value**:
   - Initializes `mini` with the first element of the list.
   - Iterates over each element in the list.
   - Compares each element with `mini`. If an element is less than `mini`, updates `mini` with this element.
3. **Return Minimum Value**: Returns `mini`, which holds the minimum value found in the list.

#### Usage Example:
```python
numbers = [8, 7, 2, 5, 3, 9, 4]
min_number = find_min(numbers)
print(min_number)
# Output: 2
```
