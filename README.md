# test-pypi-pru

[![Python Version](https://img.shields.io/badge/python-3.14+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-Proprietary-red.svg)](LICENSE)
[![Documentation](https://img.shields.io/badge/docs-Sphinx-green.svg)](https://actuaan.github.io/test_pypi_pub/latest/)

A compiled Cython package demonstrating professional packaging with scikit-build-core, complete documentation with Sphinx, and automated release workflows.

## 🚀 Features

- ✅ **Compiled with Cython** for maximum performance
- ✅ **Native binaries** - no `.py` files in distribution
- ✅ **Complete type hints** with `.pyi` stub files
- ✅ **Optimized numerical functions** with NumPy
- ✅ **DataFrame utilities** with Pandas
- ✅ **Comprehensive documentation** with Sphinx + Furo theme
- ✅ **Actuarial mathematics** support with MathJax
- ✅ **Automated versioning** with multi-version docs

## 📦 Installation

Install from Test PyPI:

```bash
pip install -i https://test.pypi.org/simple/ test-pypi-pru
```

For the stable version from PyPI (when available):

```bash
pip install test-pypi-pru
```

### Requirements

- Python >= 3.14
- NumPy >= 2.4.2
- Pandas >= 3.0.0

## 📚 Documentation

Full documentation is available at:

- **Production**: https://actuaan.github.io/test_pypi_pub/latest/
- **All versions**: https://actuaan.github.io/test_pypi_pub/

Documentation is built with **Sphinx + Furo** and includes:
- Getting Started guide
- Complete API reference with NumPy-style docstrings
- Advanced examples
- Actuarial mathematics functions with MathJax notation
- Multi-version support

### Build Documentation Locally

```bash
# Install documentation dependencies
pip install -e ".[docs]"

# Serve locally (builds and serves)
bash serve-docs.sh
# Opens at http://127.0.0.1:8000

# Or build manually
sphinx-build -b html docs/source docs/_build/html
```

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

# Actuarial mathematics
from test_pypi_pru import annuity_present_value
pv = annuity_present_value(n=10, i=0.05)
print(f"Present value: {pv:.4f}")
```

## 🏗️ Development

### Prerequisites

- Python 3.14+
- Cython >= 3.0
- CMake >= 3.20
- C++ compiler (MSVC on Windows, GCC/Clang on Unix)

### Setup

```bash
# Clone repository
git clone <your-private-repo-url>
cd test_pypi_private

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install in development mode
pip install -e ".[docs]"
```

### Build from Source

```bash
# Build wheels
python -m build

# Or use scikit-build-core directly
python -m pip install --no-build-isolation -ve .
```

### Documentation System

This project uses **Sphinx** with:
- **Furo** theme for modern UI
- **MyST-Parser** for Markdown support
- **MathJax v3** for LaTeX math rendering
- **sphinx-multiversion** for versioned docs
- Custom actuarial macros (`\ax{n}`, `\npx{k}{x}`, etc.)

## 📦 Release Process

Releases are automated via GitHub Actions:

1. **Create tag**: `git tag v0.x.x && git push --tags`
2. **Build wheels**: Automated for Windows, macOS, Linux
3. **Deploy to Test PyPI**: Automated upload
4. **Build docs**: Sphinx multi-version build
5. **Deploy docs**: Pushed to public repo `gh-pages` branch

### Security Profiles

Cython compilation uses security profiles (set via `CYTHON_SECURITY_PROFILE`):

- **DEBUG**: Full symbols, source included (development)
- **BALANCED**: Optimized, no source (default)
- **STRICT**: Maximum security, stripped binaries

## 📄 License

This project is proprietary software. See [LICENSE](LICENSE) for details.

Documentation is under separate license: [LICENSE_DOCS](LICENSE_DOCS).

## 🔗 Links

- **Documentation**: https://actuaan.github.io/test_pypi_pub/
- **Public Repository**: https://github.com/actuaan/test_pypi_pub
- **Test PyPI**: https://test.pypi.org/project/test-pypi-pru/
- **Changelog**: See [CHANGELOG.md](CHANGELOG.md) or [online docs](https://actuaan.github.io/test_pypi_pub/latest/changelog.html)

## 🙏 Acknowledgments

- Built with [scikit-build-core](https://scikit-build-core.readthedocs.io/)
- Documentation with [Sphinx](https://www.sphinx-doc.org/) and [Furo](https://pradyunsg.me/furo/)
- Type stubs with [mypy](https://mypy-lang.org/)
- Changelog with [git-cliff](https://git-cliff.org/)
