
# Numpy Examples

This repository contains a single Jupyter notebook `Numpy.ipynb` with many short examples demonstrating NumPy usage and related tools (SciPy, Matplotlib, Pandas).

## Overview
- Topics: vector and matrix operations, linear algebra (determinant, inverse, Cramer's rule), elementwise operations, norms, traces, block/Kronecker products, sparse matrices, plotting, and small Pandas/datetime examples.
- Format: the notebook is a collection of self-contained cells intended for learning and experimenting.

## Included script
I extracted and cleaned the notebook into a runnable script at `scripts/numpy_examples.py`. The script groups related examples into functions and handles errors so it can be run from a terminal.

## Dependencies
- Python 3.8+
- numpy
- scipy (optional; used in a few examples)
- matplotlib (optional; plotting examples)
- pandas (optional; DataFrame example)

Install dependencies with:

```
pip install numpy scipy matplotlib pandas
```

## Quick run
From the repository root run:

```bash
python scripts/numpy_examples.py
```

This will execute the grouped examples and print results to the console. Plots (Matplotlib) will open in windows when reached.

## Notes
- The notebook remains the primary source of the examples; use the script for quick command-line runs or converting parts into tests.

