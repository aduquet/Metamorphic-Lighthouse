### README for Min Function

#### Function Description:
The `min` function is designed to find the minimum value in a given list of numbers. It iterates through each element of the list, comparing each element with the current minimum value and updating the minimum value as needed. This function is essential in data analysis, algorithms, and general programming tasks for determining the smallest element in a collection of data.

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
   - Initializes `min_val` with the first element of the list.
   - Iterates over each element in the list.
   - Compares each element with `min_val`. If an element is less than `min_val`, updates `min_val` with this element.
3. **Return Minimum Value**: Returns `min_val`, which holds the minimum value found in the list.

#### Usage Example:
```python
numbers = [4, 7, 2, 9, 5, 1, 8]
min_number = min(numbers)
print(min_number)
# Output: 1
```
