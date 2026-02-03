## v0.6.14 (2026-02-03)

### Fix

- add global target list for compiled modules and create build_all_modules target

## v0.6.13 (2026-02-03)

### Fix

- update CMakeLists.txt and pyproject.toml for improved build configuration and debugging

## v0.6.12 (2026-02-03)

### Fix

- add debug message for module build and specify wheel install directory

## v0.6.11 (2026-02-03)

### Fix

- update wheel package path in pyproject.toml

## v0.6.10 (2026-02-03)

### Fix

- correct license field name in pyproject.toml

## v0.6.9 (2026-02-03)

### Fix

- correct license field name in pyproject.toml

## v0.6.8 (2026-02-03)

### Fix

- update license configuration in pyproject.toml for clarity

## v0.6.7 (2026-02-03)

### Fix

- update cibuildwheel version and enhance build verbosity for better debugging

## v0.6.6 (2026-02-03)

### Fix

- optimize dependency installation and update version detection logic

## v0.6.5 (2026-02-03)

### Fix

- enhance CI/CD workflow and CMake configuration for improved build efficiency

## v0.6.4 (2026-02-03)

### Fix

- correct .pyi install command to restore binary installation

## v0.6.3 (2026-02-03)

### Fix

- simplify .pyi generation by copying source files

## v0.6.2 (2026-02-03)

### Fix

- robust .pyi stub generation and installation in wheels

## v0.6.1 (2026-02-03)

### Fix

- improve stub generation process and ensure optional installation of .pyi files

## v0.6.0 (2026-02-03)

### Feat

- update func3 to compute quadratic (value + 1)^2 and adjust docstring

## v0.5.1 (2026-02-03)

### Fix

- update Python version requirement and add mypy dependency; adjust stub generation path and wheel exclusion rules

## v0.5.0 (2026-02-02)

### Feat

- enhance CMake configuration for stub generation and add requirements.txt

## v0.4.0 (2026-02-02)

### Feat

- update release workflow and CMake configuration to generate type stubs

## v0.3.0 (2026-02-02)

### Feat

- add type hint stubs for main, modulo1, and modulo2 modules

## v0.2.12 (2026-02-02)

### Fix

- remove unnecessary Cython flag for docstrings in CMake configuration

## v0.2.11 (2026-02-02)

### Fix

- add missing Salary data to sample DataFrame in modulo2.py

## v0.2.10 (2026-02-02)

### Fix

- correct func2 documentation and implementation to reflect squaring behavior

## v0.2.9 (2026-02-02)

### Fix

- update Cython installation and compilation commands for improved docstring handling

## v0.2.8 (2026-02-02)

### Refactor

- enhance docstrings across modules for clarity and consistency

## v0.2.7 (2026-02-02)

### Refactor

- update compile_py_module function to correctly generate PYX and CPP file names

## v0.2.6 (2026-02-02)

### Refactor

- update compile_py_module function to include TARGET_NAME parameter

## v0.2.5 (2026-02-02)

### Refactor

- update cibuildwheel version and specify Python builds in release workflow

## v0.2.4 (2026-02-02)

### Refactor

- update workflow to run on Windows instead of macOS

## v0.2.3 (2026-02-01)

### Refactor

- update wheel.exclude to exclude all .py files except __init__.py

## v0.2.2 (2026-02-01)

### Refactor

- remove install.components from build configuration

## v0.2.1 (2026-02-01)

### Refactor

- remove macOS universal2 architecture setting from build wheels step

## v0.2.0 (2026-02-01)

### Feat

- add support for universal2 wheels on macOS

## v0.1.8 (2026-02-01)

### Refactor

- simplify macOS build configuration in release workflow

## v0.1.7 (2026-02-01)

### Refactor

- clean up function names and imports in submodules

## v0.1.6 (2026-02-01)

### Fix

- add support for building wheels on both macOS architectures

## v0.1.5 (2026-02-01)

### Fix

- remove unnecessary wheel.py-api configuration from pyproject.toml

## v0.1.4 (2026-02-01)

### Fix

- streamline Cython compilation process by removing redundant commands

## v0.1.3 (2026-02-01)

### Fix

- update project languages in CMakeLists.txt and enhance Cython compilation process

## v0.1.2 (2026-02-01)

### Fix

- update wheel.exclude to prevent exclusion of __init__.py files

## v0.1.1 (2026-02-01)

### Fix

- update CMake version specification and remove wheel.exclude to prevent exclusion of __init__.py files

## v0.1.0 (2026-02-01)

### Feat

- add annotated_tag configuration for commitizen
- add release script for version bump and tag push
- enhance release workflow with full git history fetch and tag management
- add version provider for Commitizen configuration
- add Python setup step in release workflow and update notes with TODOs
- prueba de commitizen con push automático
- feat: prueba del workflow con cz bump
- :sparkles: Modifica el toml, yml, añade control de versiones

### Fix

- update setuptools configuration to include package data and exclude .py files from wheel
- revert version number to 0.0.2 in pyproject.toml
- revert version number to 0.0.2 in pyproject.toml
- revert version number to 0.0.2 in pyproject.toml
