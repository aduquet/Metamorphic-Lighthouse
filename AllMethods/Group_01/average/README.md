### README for Average Function

#### Function Description:
The `average` function calculates the mean (average) value of a list of numerical elements. This function iterates through each element, computes the sum, and then divides this sum by the number of elements in the list. It's designed to work with lists containing integers and floats.

#### Parameters:
- `data`: A list of numbers (integers or floats) whose average is to be calculated.

#### Returns:
- The average of all elements in the input list. Returns `None` if the list is empty, indicating that an average cannot be computed.

#### Raises:
- `TypeError`: If the input is not a list.
- `ValueError`: If any element in the list is not an integer or a float.

#### Function Logic:
1. **Input Validation**: 
   - Checks if the input `data` is a list. If not, a `TypeError` is raised.
   - Checks if the list is empty. If so, returns `None` as the average cannot be computed.
2. **Sum Calculation**:
   - Initializes a variable `sum_data` to 0.
   - Iterates through each element in the list.
   - Checks if each element is an integer or a float. If not, a `ValueError` is raised.
   - Adds each element to `sum_data`.
3. **Average Calculation**:
   - Divides `sum_data` by the number of elements in the list to find the average.
4. **Return Average**: Returns the calculated average.

#### Usage Example:
```python
numbers = [20, 30, 40, 50]
average_value = average(numbers)
print(average_value)
# Output: 35.0
```
