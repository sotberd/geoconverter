<p align="center">
    <img src="https://cdn.icon-icons.com/icons2/1532/PNG/512/3285299-orbit-orbital-satellite-shuttle-space-spaceship_106796.png" width="50%" alt="geoconverter-logo">
</p>
<p align="center">
  <a href="https://www.python.org/downloads/release/python-3110/" target="_blank">
      <img src="https://img.shields.io/badge/Python-3.11-blue?logo=python" alt="Python 3.11">
  </a>
  <a href="https://github.com/sotberd/geoconverter/actions/workflows/ci.yml?query=workflow%3ACI%3Amain" target="_blank">
    <img src="https://github.com/sotberd/geoconverter/actions/workflows/ci.yml/badge.svg?branch=main" alt="CI">
  </a>
</p>
<h1 align="center">GeoConverter</h1>
<p align="center">
    <em><strong>A CLI tool to convert geospatial data.</strong></em>
</p>

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Planned Features](#planned-features)
- [Getting Started](#getting-started)
  - [Local Development](#local-development)
  - [Running the CLI](#running-the-cli)
  - [Testing](#testing)
  - [Code Quality](#code-quality)
- [License](#license)

## Overview

**`GeoConverter`** is a command-line tool for converting geospatial data. Designed for efficiency and ease of use, it seamlessly integrates into various workflows, making geospatial data conversion straightforward.

## Features

- ✅ **CLI-based** – Simple and efficient command-line interface.
- ✅ **Convert Shapefiles to GeoJSON** – Easily transform geospatial data.

## Planned Features

The following features are planned for future releases:

- [ ] Convert GeoJSON to Shapefile
- [ ] Convert Raster to GeoJSON and Shapefile
- [ ] Convert Shapefile to Raster
- [ ] Convert GeoJSON to Raster
- [ ] Publish to PyPI for easy installation via `pip`

## Getting Started

### Local Development

To set up the project locally, follow these steps:

1. Clone this repository:

   ```bash
   git clone https://github.com/sotberd/geoconverter.git
   ```

2. Install PDM if you don't have it already. You can do this via pip:

   ```bash
   pip install pdm
   ```

3. Activate the project environment with PDM:

   ```bash
   pdm use
   ```

   You can specify the Python version if needed, or omit it to use the default one.

4. Install the project dependencies:

   ```bash
   pdm install
   ```

   This will set up the project with PDM’s environment management and install all the necessary dependencies as defined in pyproject.toml.

### Running the CLI

To run the CLI, use the following command:

```bash
geoconverter --help
```

The CLI provides a simple way to convert Shapefiles to GeoJSON. To convert Shapefiles to GeoJSON, use the following command:

```bash
geoconverter shp2geojson --input-path data/shp --output-path data/geojson --crs EPSG:4326
```

> The --output-path will be created if it does not exist. The --crs parameter is optional; The default is the original CRS of the shapefile.

### Testing

Testing is crucial for maintaining the reliability of the API. This project uses `pytest` for testing.

```bash
./scripts/test.sh

open htmlcov/index.html
```

### Code Quality

To maintain code quality, this project uses pre-commit hooks. These hooks can automatically format and lint your code before commits.

1. Run pre-commit hooks:

   ```bash
   pre-commit run --all-files
   ```

2. Formatting:

   To automatically format your code, use the following script:

   ```bash
   ./scripts/format.sh
   ```

3. Linting:

   To lint your code, use the following script:

   ```bash
   ./scripts/lint.sh
   ```

## License

This project is licensed under the terms of the [MIT](LICENCE).
