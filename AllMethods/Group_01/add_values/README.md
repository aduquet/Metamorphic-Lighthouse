### README for Add Values Function

#### Function Description:
`add_values` is a Python function that calculates the sum of all the elements in a given list. The function iterates through each element of the list, adding them to a running total, and then returns this total sum. It's a simple yet fundamental operation commonly used in various data processing and analysis tasks.

#### Parameters:
- `data`: A list of numbers (integers or floats) whose sum is to be calculated.

#### Returns:
- The sum of all elements in the input list.

#### Function Logic:
1. **Initialization**: 
   - Initializes a variable `total` to 0. This variable will accumulate the sum of all elements in the list.
2. **Sum Calculation**:
   - Iterates through each element in the list `data`.
   - Adds each element to the `total`.
3. **Return Total**: After iterating through all elements, the function returns `total`, which contains the sum of all elements in the list.

#### Usage Example:
```python
numbers = [5, 10, 15, 20]
total_sum = add_values(numbers)
print(total_sum)
# Output: 50
```
