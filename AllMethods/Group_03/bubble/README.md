### README for Bubble Sort Function

#### Function Description:
`bubble` is a Python function implementing the bubble sort algorithm to sort a list. Bubble sort is a simple comparison-based algorithm in which each pair of adjacent elements is compared, and the elements are swapped if they are not in order. This process is repeated until no swaps are needed, indicating that the list is sorted.

#### Parameters:
- `elements`: A list to be sorted. The elements of the list must be of the same type.

#### Returns:
- The sorted list.

#### Raises:
- `TypeError`: If the input is not a list.
- `ValueError`: If the list contains elements of different types.

#### Function Logic:
1. **Input Validation**: 
   - The function first checks if the input is a list.
   - It then checks if all elements in the list are of the same type.
2. **Sorting Process**:
   - The function iterates through the list multiple times.
   - For each pass, it compares adjacent elements and swaps them if they are in the wrong order (the first element is greater than the second).
   - This process is repeated, decreasing the number of elements to compare in each pass (as the largest elements "bubble" to the end of the list).
3. **Return Sorted List**: Once the passes are completed without any swaps, the list is sorted and returned.

#### Usage Example:
```python
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble(unsorted_list)
print(sorted_list)
# Output: [11, 12, 22, 25, 34, 64, 90]
```

#### Note:
Bubble sort is known for its simplicity but is inefficient for large lists compared to more advanced sorting algorithms like quicksort, mergesort, or heapsort. It is best used for small lists or for educational purposes to understand basic sorting concepts.