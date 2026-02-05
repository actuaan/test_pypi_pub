# Test PyPI Pru

Welcome to the documentation for **test_pypi_pru**, a Python project compiled with Cython demonstrating professional packaging with scikit-build-core.

## 🚀 Features

- ✅ **Compiled with Cython** for maximum performance
- ✅ **Native binaries** - no `.py` files in distribution
- ✅ **Complete type hints** with `.pyi` stub files
- ✅ **Optimized numerical functions** with NumPy
- ✅ **DataFrame utilities** with Pandas

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

- Python >= 3.11
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

## 📚 Package Structure

```
test_pypi_pru/
├── main.py           # Main function
├── sub1/
│   └── modulo1.py   # Numerical functions
└── sub2/
    └── modulo2.py   # DataFrame utilities
```

## 🔗 Links

- [GitHub Repository](https://github.com/actuaan/test_pypi_pub)
- [Test PyPI Package](https://test.pypi.org/project/test-pypi-pru/)
- [Getting Started Guide](getting-started.md)
- [Complete API Reference](api/main.md)

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/actuaan/test_pypi_pub/blob/main/LICENSE) file for details.
