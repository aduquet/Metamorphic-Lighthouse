### README for Count Non-Zeros Function

#### Function Description:
The `cnt_non_zeros` function counts the number of non-zero elements in a list. This function iterates through the list and increments a counter each time it encounters an element that is not equal to zero. This operation is common in data analysis and processing tasks, especially when determining the presence of non-zero or significant values in a dataset.

#### Parameters:
- `a`: A list of elements. The elements can be of any type, but the function specifically checks for non-zero numerical values.

#### Returns:
- The count of non-zero elements in the list.

#### Function Logic:
1. **Counter Initialization**: 
   - Initializes a counter `cnt` to 0. This counter will track the number of non-zero elements.
2. **Iterate and Count**:
   - Iterates through each element in the list using a `for` loop.
   - Checks if the current element is not equal to zero.
   - If the element is non-zero, increments the counter `cnt`.
3. **Return Count**: After completing the iteration, the function returns the value of `cnt`, indicating the number of non-zero elements found.

#### Usage Example:
```python
data = [0, 1, 2, 0, 3, 0, 4, 5]
non_zero_count = cnt_non_zeros(data)
print(non_zero_count)
# Output: 5
```
