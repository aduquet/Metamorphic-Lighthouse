### README for Sum Function

#### Function Description:
The `sum` function calculates the sum of a list of numerical values. It provides a straightforward way to obtain the total sum of elements in a list. This function is a fundamental operation in data analysis, mathematics, and various programming tasks where aggregating numerical values is required.

#### Parameters:
- `values`: A list of numerical elements (integers or floats).

#### Returns:
- The sum of all elements in the list as a numerical value.

#### Raises:
- `TypeError`: If the input is not a list or if the list contains non-numeric elements.
- `ValueError`: None

#### Function Logic:
1. **Input Validation**: 
   - Checks if the input `values` is a list and contains only numeric elements. If not, raises the appropriate `TypeError`.
2. **Summation Calculation**:
   - Initializes a variable `total` to zero.
   - Iterates through each element in the list and adds it to the `total` variable.
3. **Return Summation**: Returns the `total` value, which represents the sum of all elements in the list.

#### Usage Example:
```python
numbers = [1, 2, 3, 4, 5]
result = sum(numbers)
print(result)
# Output: 15
```
