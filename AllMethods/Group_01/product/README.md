### README for Product Function

#### Function Description:
The `product` function calculates the product of all the elements in a given list of numbers. It is a fundamental function in mathematics and programming, useful in scenarios where you need to multiply a series of numbers together, such as calculating the factorial of a number, or in financial calculations involving compound interest.

#### Parameters:
- `data`: A list of numerical elements (integers or floats).

#### Returns:
- The product of all elements in the list.

#### Raises:
- `TypeError`: If the input is not a list, or if the list contains elements that are not integers or floats.
- `ValueError`: If the list is empty.

#### Function Logic:
1. **Input Validation**: 
   - Checks if the input `data` is a list and contains only numerical elements. If not, raises the appropriate `TypeError`.
   - Checks if the list `data` is empty. If so, raises a `ValueError`, as the product cannot be determined in an empty list.
2. **Calculating Product**:
   - Initializes `prod` to 1 (the identity element for multiplication).
   - Iterates over each element in the list.
   - Multiplies each element to `prod`.
3. **Return Product**: Returns `prod`, which holds the product of all the values in the list.

#### Usage Example:
```python
numbers = [2, 3, 4, 5]
product_value = product(numbers)
print(product_value)
# Output: 120
```
