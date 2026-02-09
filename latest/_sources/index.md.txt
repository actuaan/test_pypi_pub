# test-pypi-pru Documentation

Welcome to the documentation for **test-pypi-pru**, a compiled Cython package demonstrating professional packaging with scikit-build-core.

## 🚀 Features

- ✅ **Compiled with Cython** for maximum performance
- ✅ **Native binaries** - no `.py` files in distribution
- ✅ **Complete type hints** with `.pyi` stub files
- ✅ **Optimized numerical functions** with NumPy
- ✅ **DataFrame utilities** with Pandas
- ✅ **Actuarial mathematics** support with MathJax

## 📦 Installation

Install the package from Test PyPI:

```bash
pip install -i https://test.pypi.org/simple/ test-pypi-pru
```

For the stable version from PyPI (when available):

```bash
pip install test-pypi-pru
```

### Requirements

- Python >= 3.10
- NumPy >= 2.4.2
- Pandas >= 3.0.0

## 🎯 Quick Start

```python
from test_pypi_pru import func1, func2, get_dataframe, my_function
import numpy as np

# Numerical operations
data = np.array([1, 2, 3, 4, 5])
squared = func1(data)
print(squared)  # [1 4 9 16 25]

# Working with DataFrames
df = get_dataframe()
print(df)

# Main function
result = my_function(5, 3)
print(result)  # 15
```

## 📚 Documentation Contents

```{toctree}
:maxdepth: 2
:caption: User Guide

getting-started
examples
```

```{toctree}
:maxdepth: 2
:caption: API Reference

api/main
api/sub1
api/sub2
```

```{toctree}
:maxdepth: 1
:caption: About

changelog
```

## Indices and Tables

- {ref}`genindex`
- {ref}`modindex`
- {ref}`search`
