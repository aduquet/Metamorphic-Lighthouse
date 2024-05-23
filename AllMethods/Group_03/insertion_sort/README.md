### README for Insertion Sort Function

#### Function Description:
`insertion_sort` is a Python function that implements the insertion sort algorithm to sort a list of numbers in ascending order. Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort. However, it provides a simple and easy-to-understand approach to sorting.

#### Parameters:
- `arrays`: A list of numbers (integers or floats).

#### Returns:
- A list sorted in ascending order.

#### Raises:
- `TypeError`: If the input is not a list.
- `TypeError`: If the list contains elements other than numbers (integers or floats).

#### Function Logic:
1. **Input Validation**: The function first checks if the input is a list and if all elements in the list are numbers (either integers or floats).
2. **Sorting Process**:
   - The function iterates through each element in the list starting from the second element.
   - For each element, it compares it with the elements before it, moving each element one position to the right if it is larger than the current element.
   - The process is repeated until the current element is placed in its correct position.
   - This process results in the elements before the current element being sorted.
3. **Return Sorted List**: After completing the iteration for all elements, the function returns the sorted list.

#### Usage Example:
```python
unsorted_list = [34, 2, 1, 78, 6, 45]
sorted_list = insertion_sort(unsorted_list)
print(sorted_list)
# Output: [1, 2, 6, 34, 45, 78]
```

