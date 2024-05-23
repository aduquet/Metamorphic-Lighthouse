# ListDescripter

`ListDescripter` is a Python class designed to analyze and describe properties of a list of numbers without the need for additional computations between the elements in the list. It provides a set of methods to extract various characteristics and properties of the list.

## Methods

### `get_length()`

Returns the length (number of elements) of the list.

### `has_zero()`

Checks if the list contains the value zero and returns `True` if it does, otherwise returns `False`.

### `cnt_positive_numbers()`

Counts and returns the number of positive numbers in the list.

### `cnt_negative_numbers()`

Counts and returns the number of negative numbers in the list.

### `get_minimum()`

Returns the minimum value in the list.

### `get_maximum()`

Returns the maximum value in the list.

### `get_sum()`

Calculates and returns the sum of all elements in the list.

### `get_mean()`

Calculates and returns the mean (average) of the elements in the list.

### `get_median()`

Calculates and returns the median of the elements in the list.

### `get_range()`

Calculates and returns the range of the list, which is the difference between the maximum and minimum values.

### `has_duplicates()`

Checks if the list contains any duplicate values and returns `True` if it does, otherwise returns `False`.

### `is_sorted()`

Determines whether the list is sorted in ascending order and returns `True` if it is, otherwise returns `False`.

### `count_distinct_values()`

Counts and returns the number of distinct (unique) values in the list.

### `contains_even_numbers()`

Checks if the list contains any even numbers and returns `True` if it does, otherwise returns `False`.

### `contains_odd_numbers()`

Checks if the list contains any odd numbers and returns `True` if it does, otherwise returns `False`.

### `contains_integers()`

Checks if all elements in the list are integers and returns `True` if they are, otherwise returns `False`.

## Usage

To use the `ListDescripter` class, create an instance of it with your list of numbers, and then call the methods to extract the desired properties of the list. For example:

```python
my_list = [1, 2, -4, 0]
descripter = ListDescripter(my_list)

print("Length:", descripter.get_length())
print("Contains Zero:", descripter.has_zero())
print("Count of Positive Numbers:", descripter.cnt_positive_numbers())
# ... (continue with other method calls)
