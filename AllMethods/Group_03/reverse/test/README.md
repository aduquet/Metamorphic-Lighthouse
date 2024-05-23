
# Testing `reverse` Function

This repository provides a suite of tests for the `reverse` function, which returns the reversed version of a given list.

## Tests Explanation:

- `test_reverse_list_of_integers`: Tests reversing a list of integers.
- `test_reverse_single_element`: Tests reversing a list with a single element.
- `test_reverse_list_of_strings`: Tests reversing a list of strings.
- `test_empty_list`: Tests the function's response to an empty list.
- `test_invalid_input_string`: Tests the function's response when given a string instead of a list.

## Running the Tests:

You can run the tests in different ways:

1. **Using unittest from Command Line**:
   ```bash
   python3 -m unittest test_reverse.py
   ```

2. **Running the Script Directly**:
   ```bash
   python3 test_reverse.py
   ```

For a more verbose output detailing each test method and its result, add `-v` to the command:
   ```bash
   python3 -m unittest -v test_reverse.py
   ```

Ensure that the `reverse_function.py` is in the same directory as the test script.
```

