# Changelog

All notable changes to this project are documented below.
## **[0.14.0]** <small>February 06, 2026</small> { id="0.14.0" }


### Fixed

- Update git clone command to fetch all branches for public repo sync (`3c59c76`)
- Update changelog template to handle unknown dates correctly (`cd6395f`)

### Added

- Enhance changelog generation by adding tag verification and minimal changelog fallback (`ac05d9e`)
- Enhance git-cliff installation by improving version extraction and URL construction (`93912dd`)
- Improve git-cliff installation by fetching the latest release version dynamically (`e7d2c05`)
## **[0.13.0]** <small>February 06, 2026</small> { id="0.13.0" }


### Added

- Feat: add documentation and public repo sync workflow with changelog generation and deployment
refactor: update release workflow to separate documentation build and public repo sync steps (`291cf1d`)
## **[0.12.0]** <small>February 06, 2026</small> { id="0.12.0" }


### Added

- Update git-cliff installation to use the latest version and improve binary detection (`edf7153`)
## **[0.11.0]** <small>February 06, 2026</small> { id="0.11.0" }


### Added

- Enhance documentation workflow with improved caching, error handling, and changelog generation (`8bfc4b4`)
## **[0.10.0]** <small>February 06, 2026</small> { id="0.10.0" }


### Added

- Enhance documentation generation with changelog and new plugins (`e4ad8bd`)
## **[0.9.0]** <small>February 05, 2026</small> { id="0.9.0" }


### Added

- Generate versions.json for available versions in documentation (`7c1c3ac`)
## **[0.8.4]** <small>February 05, 2026</small> { id="0.8.4" }


### Fixed

- Streamline documentation deployment process in release workflow (`14b2ecb`)
- Remove wheel validation step before publishing to Test PyPI (`31ac50c`)
## **[0.8.3]** <small>February 05, 2026</small> { id="0.8.3" }


### Fixed

- Comment out wheel validation step before publishing (`f932ca6`)
## **[0.8.2]** <small>February 05, 2026</small> { id="0.8.2" }


### Fixed

- Update scikit-build-core version and clarify license-files entry in pyproject.toml (`eefd94f`)
## **[0.8.1]** <small>February 05, 2026</small> { id="0.8.1" }


### Fixed

- Correct license-files entry in pyproject.toml (`30759de`)
## **[0.8.0]** <small>February 05, 2026</small> { id="0.8.0" }


### Added

- Update release workflow, enhance license information, and improve project metadata (`88c95af`)
## **[0.7.2]** <small>February 05, 2026</small> { id="0.7.2" }


### Fixed

- Update repository URLs to reflect new owner and improve documentation references (`3cce573`)
## **[0.7.1]** <small>February 04, 2026</small> { id="0.7.1" }


### Fixed

- Update docs deployment to clone and copy instead of remote push (`4193542`)
## **[0.7.0]** <small>February 04, 2026</small> { id="0.7.0" }


### Fixed

- Update dependencies in pyproject.toml to specify minimum versions for pandas and numpy (`7368363`)
- Streamline version detection logic in __init__.py (`89eed72`)

### Added

- Enhance documentation and setup for mkdocs with new guides and examples (`739e19e`)

### Changed

- Update section headers and improve clarity in notas.md (`9c0afcc`)
## **[0.6.17]** <small>February 03, 2026</small> { id="0.6.17" }


### Fixed

- Correct install(TARGETS) for Python MODULE libraries (`59fcd2b`)
## **[0.6.16]** <small>February 03, 2026</small> { id="0.6.16" }


### Fixed

- Update installation paths in CMakeLists.txt to use SKBUILD_PLATLIB_DIR and remove wheel.packages from pyproject.toml (`8e8fbcf`)
## **[0.6.15]** <small>February 03, 2026</small> { id="0.6.15" }


### Fixed

- Update compile_py_module function to use subdirectories for avoiding collisions (`9e2dc52`)
## **[0.6.14]** <small>February 03, 2026</small> { id="0.6.14" }


### Fixed

- Add global target list for compiled modules and create build_all_modules target (`407e140`)
## **[0.6.13]** <small>February 03, 2026</small> { id="0.6.13" }


### Fixed

- Update CMakeLists.txt and pyproject.toml for improved build configuration and debugging (`41c9415`)
## **[0.6.12]** <small>February 03, 2026</small> { id="0.6.12" }


### Fixed

- Add debug message for module build and specify wheel install directory (`146781c`)
## **[0.6.11]** <small>February 03, 2026</small> { id="0.6.11" }


### Fixed

- Update wheel package path in pyproject.toml (`c0e22ea`)
## **[0.6.10]** <small>February 03, 2026</small> { id="0.6.10" }


### Fixed

- Correct license field name in pyproject.toml (`74d2a72`)
## **[0.6.9]** <small>February 03, 2026</small> { id="0.6.9" }


### Fixed

- Correct license field name in pyproject.toml (`8d461f7`)
## **[0.6.8]** <small>February 03, 2026</small> { id="0.6.8" }


### Fixed

- Update license configuration in pyproject.toml for clarity (`2a70c78`)
## **[0.6.7]** <small>February 03, 2026</small> { id="0.6.7" }


### Fixed

- Update cibuildwheel version and enhance build verbosity for better debugging (`d567627`)
## **[0.6.6-retry]** <small>February 03, 2026</small> { id="0.6.6-retry" }


### Fixed

- Optimize dependency installation and update version detection logic (`058402f`)
## **[0.6.5-retry]** <small>February 03, 2026</small> { id="0.6.5-retry" }


### Fixed

- Enhance CI/CD workflow and CMake configuration for improved build efficiency (`0c6dd6f`)
## **[0.6.4]** <small>February 03, 2026</small> { id="0.6.4" }


### Fixed

- Correct .pyi install command to restore binary installation (`1ab7dc2`)
## **[0.6.3]** <small>February 03, 2026</small> { id="0.6.3" }


### Fixed

- Simplify .pyi generation by copying source files (`65cca03`)
## **[0.6.2]** <small>February 03, 2026</small> { id="0.6.2" }


### Fixed

- Robust .pyi stub generation and installation in wheels (`5968a80`)
## **[0.6.1]** <small>February 03, 2026</small> { id="0.6.1" }


### Fixed

- Improve stub generation process and ensure optional installation of .pyi files (`46a5b8a`)
## **[0.6.0]** <small>February 03, 2026</small> { id="0.6.0" }


### "fix

- Use Python module invocation for stubgen in CMake" (`939580b`)

### Added

- Update func3 to compute quadratic (value + 1)^2 and adjust docstring (`3cf0bd0`)
## **[0.5.1]** <small>February 03, 2026</small> { id="0.5.1" }


### Fixed

- Update Python version requirement and add mypy dependency; adjust stub generation path and wheel exclusion rules (`92456f0`)
## **[0.5.0]** <small>February 02, 2026</small> { id="0.5.0" }


### Added

- Enhance CMake configuration for stub generation and add requirements.txt (`422386d`)
## **[0.4.0]** <small>February 02, 2026</small> { id="0.4.0" }


### Added

- Update release workflow and CMake configuration to generate type stubs (`1604a65`)
## **[0.3.0]** <small>February 02, 2026</small> { id="0.3.0" }


### Added

- Add type hint stubs for main, modulo1, and modulo2 modules (`2125282`)
## **[0.2.12]** <small>February 02, 2026</small> { id="0.2.12" }


### Fixed

- Remove unnecessary Cython flag for docstrings in CMake configuration (`e9f0221`)
## **[0.2.11]** <small>February 02, 2026</small> { id="0.2.11" }


### Fixed

- Add missing Salary data to sample DataFrame in modulo2.py (`9945e6e`)

### Chores

- Add docstring verification step in release workflow and update Cython flags for better docstring handling (`be9437f`)
## **[0.2.10]** <small>February 02, 2026</small> { id="0.2.10" }


### Fixed

- Correct func2 documentation and implementation to reflect squaring behavior (`83cb8d0`)

### Chores

- Add Cython directives for docstring handling in main and module files (`487c313`)
## **[0.2.9]** <small>February 02, 2026</small> { id="0.2.9" }


### Fixed

- Update Cython installation and compilation commands for improved docstring handling (`da55558`)
## **[0.2.8]** <small>February 02, 2026</small> { id="0.2.8" }


### Changed

- Enhance docstrings across modules for clarity and consistency (`b107f22`)
## **[0.2.7]** <small>February 02, 2026</small> { id="0.2.7" }


### Changed

- Update compile_py_module function to correctly generate PYX and CPP file names (`8b20fb7`)
## **[0.2.6]** <small>February 02, 2026</small> { id="0.2.6" }


### Changed

- Update compile_py_module function to include TARGET_NAME parameter (`77c6a9d`)
## **[0.2.5]** <small>February 02, 2026</small> { id="0.2.5" }


### Changed

- Update cibuildwheel version and specify Python builds in release workflow (`6381284`)
## **[0.2.4]** <small>February 02, 2026</small> { id="0.2.4" }


### Changed

- Update workflow to run on Windows instead of macOS (`384ea4f`)
## **[0.2.3]** <small>February 01, 2026</small> { id="0.2.3" }


### Changed

- Update wheel.exclude to exclude all .py files except __init__.py (`0bc3734`)
## **[0.2.2]** <small>February 01, 2026</small> { id="0.2.2" }


### Changed

- Remove install.components from build configuration (`5eb879c`)
## **[0.2.1]** <small>February 01, 2026</small> { id="0.2.1" }


### Changed

- Remove macOS universal2 architecture setting from build wheels step (`1ee93ed`)
## **[0.2.0]** <small>February 01, 2026</small> { id="0.2.0" }


### Added

- Add support for universal2 wheels on macOS (`6be80bb`)
## **[0.1.8]** <small>February 01, 2026</small> { id="0.1.8" }


### Changed

- Simplify macOS build configuration in release workflow (`a5bb9fb`)
## **[0.1.7]** <small>February 01, 2026</small> { id="0.1.7" }


### Changed

- Clean up function names and imports in submodules (`1b8e107`)
## **[0.1.6]** <small>February 01, 2026</small> { id="0.1.6" }


### Fixed

- Add support for building wheels on both macOS architectures (`0b2c5ef`)
## **[0.1.5]** <small>February 01, 2026</small> { id="0.1.5" }


### Fixed

- Remove unnecessary wheel.py-api configuration from pyproject.toml (`3fb4a72`)
## **[0.1.4]** <small>February 01, 2026</small> { id="0.1.4" }


### Fixed

- Streamline Cython compilation process by removing redundant commands (`52ad4eb`)
## **[0.1.3]** <small>February 01, 2026</small> { id="0.1.3" }


### Fixed

- Update project languages in CMakeLists.txt and enhance Cython compilation process (`f38a217`)
## **[0.1.2]** <small>February 01, 2026</small> { id="0.1.2" }


### Fixed

- Update wheel.exclude to prevent exclusion of __init__.py files (`f405877`)
## **[0.1.1]** <small>February 01, 2026</small> { id="0.1.1" }


### Fixed

- Update CMake version specification and remove wheel.exclude to prevent exclusion of __init__.py files (`f40b4ff`)

### Chores

- Update CHANGELOG.md for version 0.1.0 and enable changelog update on version bump (`0f0a916`)
## **[0.1.0]** <small>February 01, 2026</small> { id="0.1.0" }


### Fixed

- Update setuptools configuration to include package data and exclude .py files from wheel (`2ce3831`)
- Revert version number to 0.0.2 in pyproject.toml (`a4b78a9`)
- Revert version number to 0.0.2 in pyproject.toml (`02bae0c`)
- Revert version number to 0.0.2 in pyproject.toml (`30092d6`)

### Chores

- Clean up CHANGELOG.md by removing outdated version entries (`200e949`)
- Move Commitizen version bump to build_wheels job (`10a961f`)
- Chore: prueba del workflow con commitizen (`81c051a`)
- :rocket: release v0.0.2 (`d7b29da`)
- :rocket: release v0.0.1 (`5e78403`)
- :rocket: release 0.0.4 (`76d9a73`)

### Documentation

- Enhance documentation and add functions in latuca package; include docstrings for modules and functions (`39276ad`)
- Update release workflow to use new token and improve file copying logic; enhance repository notes and add documentation file (`82051e5`)

### Added

- Add annotated_tag configuration for commitizen (`7ece40d`)
- Add release script for version bump and tag push (`d9c49ed`)
- Enhance release workflow with full git history fetch and tag management (`5bef19d`)
- Add version provider for Commitizen configuration (`0b0df00`)
- Add Python setup step in release workflow and update notes with TODOs (`6591468`)
- Prueba de commitizen con push automático (`16acb33`)
- Feat: prueba del workflow con cz bump (`227fd82`)
- :sparkles: Modifica el toml, yml, añade control de versiones (`a0b872f`)
- Add permissions section to release-drafter workflow for content write access (`45ca3e2`)
- Add func_3 to sub1.modulo1 and update exports in __init__.py (`7b5c4a2`)
- Add Release Drafter configuration and enhance release workflow with pip caching (`a3c57db`)
- Add initial implementation of test_pypi_pru package with modules and functions (`49be867`)
- Add initial implementation of latuca package with modules and functions (`bcb2590`)
- Add VSCode settings for pinned GitHub Actions workflows (`2076969`)
- Add initial project structure with CMake configuration, GitHub Actions workflow, and example modules (`0a96371`)

### Changed

- Update func2 to double the input value before rounding (`29ac808`)
- Update workflow to publish to Test PyPI with specified repository URL (`f8a054f`)
- Update workflow name for clarity: 'Release and Sync Public' to 'Release in test-PyPI and Sync Public' (`466c479`)
- Update Windows environment variables in GitHub Actions and remove unnecessary pandas dependency from pyproject.toml (`f8909da`)
- Enhance GitHub Actions workflow: add Windows-specific configurations and cleanup steps (`3df4857`)
- Enhance compile_py_module function: add custom command to generate .pyx file from .py source (`fcc9ba7`)
- Enhance CMake configuration: ensure target is treated as C++ for linking in compile_py_module function (`3c3d976`)
- Update build step in release workflow to install specific dependencies for wheel building (`4710a8e`)
- Update repository URL in notes and add verification steps (`5369149`)
