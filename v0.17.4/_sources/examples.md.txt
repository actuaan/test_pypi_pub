# Detailed Examples

This page contains advanced usage examples of the `test_pypi_pru` package.

## Scientific Data Processing

### Statistical Analysis with NumPy

```python
import numpy as np
from test_pypi_pru import func1, func2

# Generate sample data
np.random.seed(42)
data = np.random.randn(1000)

# Calculate basic statistics
mean = data.mean()
std = data.std()

print(f"Mean: {mean:.4f}")
print(f"Standard deviation: {std:.4f}")

# Normalize and square
normalized = (data - mean) / std
squared = func1(normalized)

print(f"Mean of normalized squares: {squared.mean():.4f}")
```

### Batch Processing

```python
import numpy as np
from test_pypi_pru import func1

# Process data in batches to optimize memory
def process_large_dataset(total_size, batch_size=10000):
    results = []

    for i in range(0, total_size, batch_size):
        # Generate batch
        batch = np.arange(i, min(i + batch_size, total_size))

        # Process with func1
        processed = func1(batch)

        # Accumulate results
        results.append(processed.sum())

    return np.array(results)

# Process 1 million numbers in batches of 10k
batch_results = process_large_dataset(1_000_000)
print(f"Total: {batch_results.sum()}")
```

## Data Analysis with Pandas

### Complete Data Pipeline

```python
import pandas as pd
from test_pypi_pru import get_dataframe, get_average_age

# Get base data
df = get_dataframe()

# Add calculated column
df['Age_Squared'] = df['Age'] ** 2

# Filter and sort
young_people = df[df['Age'] < 32].sort_values('Age')
print(young_people)

# Calculate average of subset
avg = get_average_age(young_people)
print(f"Average age of people < 32: {avg}")
```

### Working with Custom Data

```python
import pandas as pd
from test_pypi_pru import get_average_age

# Create custom dataset
employees = pd.DataFrame({
    'Name': ['Ana', 'Juan', 'María', 'Pedro', 'Lucía'],
    'Age': [28, 35, 42, 31, 29],
    'Department': ['IT', 'HR', 'IT', 'Sales', 'IT'],
    'Salary': [50000, 45000, 60000, 48000, 52000]
})

# Analysis by department
for dept in employees['Department'].unique():
    dept_data = employees[employees['Department'] == dept]
    avg_age = get_average_age(dept_data)
    avg_salary = dept_data['Salary'].mean()

    print(f"{dept}:")
    print(f"  Average age: {avg_age:.1f}")
    print(f"  Average salary: ${avg_salary:,.0f}")
```

## Combining Functionalities

### Complete Analysis Pipeline

```python
import numpy as np
import pandas as pd
from test_pypi_pru import func1, func2, get_dataframe, get_average_age

# 1. Get data
df = get_dataframe()

# 2. Calculate average age
avg_age = get_average_age(df)
print(f"Average age: {avg_age}")

# 3. Normalize ages using NumPy
ages_array = df['Age'].values
normalized_ages = (ages_array - avg_age) / ages_array.std()

# 4. Calculate squared deviations
squared_deviations = func1(normalized_ages)

# 5. Add results to DataFrame
df['Normalized_Age'] = normalized_ages
df['Squared_Deviation'] = squared_deviations

# 6. Round values for presentation
df['Squared_Deviation_Rounded'] = df['Squared_Deviation'].apply(
    lambda x: func2(x, decimals=3)
)

print(df)
```

### Data Validation

```python
import numpy as np
from test_pypi_pru import func1, func2

def validate_and_process(data, max_value=100):
    """
    Validate and process a data array.
    """
    # Validate type
    if not isinstance(data, np.ndarray):
        data = np.array(data)

    # Validate range
    if (data > max_value).any():
        raise ValueError(f"Data exceeds maximum allowed: {max_value}")

    # Process: square
    processed = func1(data)

    # Normalize result
    max_processed = processed.max()
    normalized = processed / max_processed

    # Round each element
    rounded = np.array([
        func2(val, decimals=4) for val in normalized
    ])

    return rounded

# Usage
test_data = np.array([10, 20, 30, 40, 50])
result = validate_and_process(test_data)
print(result)
```

## Performance Optimization

### Performance Comparison

```python
import time
import numpy as np
from test_pypi_pru import func1

# Compare performance: Cython vs pure Python
sizes = [1000, 10000, 100000, 1000000]

for size in sizes:
    data = np.arange(size, dtype=float)

    # With compiled function (Cython)
    start = time.time()
    result_cython = func1(data)
    time_cython = time.time() - start

    # Pure Python
    start = time.time()
    result_python = np.square(data)
    time_python = time.time() - start

    speedup = time_python / time_cython
    print(f"Size: {size:>7} | "
          f"Cython: {time_cython:.6f}s | "
          f"Python: {time_python:.6f}s | "
          f"Speedup: {speedup:.2f}x")
```

## Real-World Use Cases

### Scoring System

```python
import pandas as pd
import numpy as np
from test_pypi_pru import func1, get_average_age

# Student data
students = pd.DataFrame({
    'Name': ['Ana', 'Bob', 'Carlos', 'Diana'],
    'Age': [20, 22, 21, 23],
    'Score': [85, 90, 78, 92]
})

# Normalize scores by age
avg_age = get_average_age(students)
age_factor = students['Age'] / avg_age

# Apply quadratic penalty
penalty = func1(age_factor - 1)  # Penalize deviation from average age

# Calculate adjusted score
students['Adjusted_Score'] = students['Score'] * (1 - 0.1 * penalty)

print(students[['Name', 'Score', 'Adjusted_Score']])
```

## Next Steps

Need more help? Check the [Complete API Reference](api/main.md) for detailed documentation of all functions.
