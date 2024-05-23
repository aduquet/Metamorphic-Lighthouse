### README for Square Function

#### Function Description:
The `square` function is designed to compute the square of each element in a given list of numbers. This function is applicable to lists containing numerical data types (integers and floats). It iterates through each element of the list, calculates its square, and returns a new list with these squared values.

#### Parameters:
- `data`: A list of numbers (integers or floats) to be squared.

#### Returns:
- A list containing the square of each element from the input list.

#### Raises:
- `TypeError`: If the input is not a list.
- `ValueError`: If the list contains elements other than numbers (integers or floats).

#### Function Logic:
1. **Input Validation**: 
   - The function first checks whether the input `data` is a list. If it is not, a `TypeError` is raised.
   - Next, it checks if all elements in the list are either integers or floats. If any element is not a number, a `ValueError` is raised.
2. **Square Calculation**:
   - The function uses a list comprehension to iterate over each element in the list.
   - Each element is squared (`x**2`) and the result is stored in a new list.
3. **Return Squared List**: The function returns the new list containing the squared values of each element from the input list.

#### Usage Example:
```python
numbers = [2, 3, 4, 5]
squared_numbers = square(numbers)
print(squared_numbers)
# Output: [4, 9, 16, 25]
```

#### Note:
This function is specifically designed for lists containing numerical values and will not work with lists containing non-numerical elements. It is an efficient way to apply a simple mathematical operation (squaring) to a collection of numerical data.