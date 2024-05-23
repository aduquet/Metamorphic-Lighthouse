### README for Find Median Function

#### Function Description:
The `find_median` function calculates the median of a list of numbers. The median is the middle value in a sorted list of numbers, providing a significant measure of the central tendency of the data. This function is widely used in statistics, data analysis, and various fields where understanding the central position of a data set is crucial.

#### Parameters:
- `data`: A list of numerical elements (integers or floats).

#### Returns:
- The median of the list as a float or integer.

#### Raises:
- `TypeError`: If the input is not a list.
- `ValueError`: If the list is empty.
- `ValueError`: If the list contains elements that are not numbers.

#### Function Logic:
1. **Input Validation**: 
   - Checks if the input `data` is a list of numbers. If not, the appropriate `TypeError` or `ValueError` is raised.
2. **Sorting the Data**:
   - Sorts the list `data` in ascending order to prepare for median calculation.
3. **Median Calculation**:
   - Determines the length of the sorted list.
   - If the length is even, calculates the median as the average of the two middle numbers.
   - If the length is odd, selects the middle number as the median.
4. **Return Median**: Returns the calculated median value.

#### Usage Example:
```python
numbers = [7, 5, 3, 1, 9]
median_value = find_median(numbers)
print(median_value)
# Output: 5
```
