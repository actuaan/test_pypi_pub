# Getting Started

This guide will help you get started using **test_pypi_pru** in your Python projects.

## Installation

First, install the package from Test PyPI:

```bash
pip install -i https://test.pypi.org/simple/ test-pypi-pru
```

## Import the Package

You can import individual functions or the entire package:

```python
# Import specific functions
from test_pypi_pru import func1, func2, func3
from test_pypi_pru import get_dataframe, get_average_age
from test_pypi_pru import my_function

# Or import the entire package
import test_pypi_pru as tpp
```

## Basic Examples

### 1. Numerical Operations with NumPy

The `sub1` module provides optimized functions for NumPy arrays:

```python
import numpy as np
from test_pypi_pru import func1, func2, func3

# func1: Square elements of an array
data = np.array([1, 2, 3, 4, 5])
squared = func1(data)
print(squared)
# Output: [ 1  4  9 16 25]

# func2: Square and round
value = 3.14159
rounded = func2(value, decimals=2)
print(rounded)
# Output: 9.87

# func3: Compute quadratic (value + 1)^2
result = func3(2.5)
print(result)
# Output: 12.25
```
reversed_text = func3(text)
print(reversed_text)
# Output: 'nohtyP'
```

### 2. Working with Pandas DataFrames

The `sub2` module provides utilities for working with DataFrames:

```python
from test_pypi_pru import get_dataframe, get_average_age

# Get a sample DataFrame
df = get_dataframe()
print(df)
# Output:
#     Name  Age      City
# 0  Alice   25  New York
# 1    Bob   30    London
# 2  Charlie 35     Paris

# Calculate average age
avg_age = get_average_age(df)
print(f"Average age: {avg_age}")
# Output: Average age: 30.0
```

### 3. Main Function

The main function of the package:

```python
from test_pypi_pru import my_function

# Multiply two numbers
result = my_function(5, 3)
print(result)
# Output: 15

# Note: Despite the "sum" name in the docstring,
# this function performs multiplication using np.prod
```

## Advanced Usage

### Working with Large Arrays

```python
import numpy as np
from test_pypi_pru import func1

# Process a large array
large_array = np.arange(1_000_000)
squared = func1(large_array)

print(f"Sum of squares: {squared.sum()}")
# Operations are optimized with Cython for better performance
```

### Data Processing with Pandas

```python
import pandas as pd
from test_pypi_pru import get_average_age

# Use with your own data
my_data = pd.DataFrame({
    'Name': ['David', 'Emma', 'Frank'],
    'Age': [28, 32, 45],
    'City': ['Berlin', 'Madrid', 'Rome']
})

average = get_average_age(my_data)
print(f"Average age in my dataset: {average}")
```

## Verify Installation

To verify that the package is correctly installed:

```python
import test_pypi_pru
print(test_pypi_pru.__version__)
# Output: 0.6.17
```

## Next Steps

- Explore the [Complete API Reference](api/main.md) to see all available functions
- Review the [Detailed Examples](examples.md) with more complex use cases
- Check the [source code on GitHub](https://github.com/actuaan/test_pypi_pub)

## Troubleshooting

### Import Error

If you encounter import errors:

```python
# ❌ Incorrect
from test_pypi_pru import func4  # Does not exist

# ✅ Correct
from test_pypi_pru import get_dataframe
```

See the [API Reference](api/main.md) for available functions.

### Performance Issues

If you experience performance issues with large arrays:

1. Make sure you're using NumPy >= 2.4.2
2. Verify the package was installed correctly (must be compiled)
3. Consider using contiguous arrays in memory with `np.ascontiguousarray()`
