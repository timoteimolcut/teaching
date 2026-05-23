# Teaching — Python Learning Repository

A hands-on Python learning repository covering fundamentals, OOP, module structure, and data analysis with Pandas.

---

## Prerequisites

- [Conda](https://docs.conda.io/en/latest/) (Miniconda or Anaconda)
- Python 3.10+

---

## Setup

1. Create and activate a conda environment:

```bash
conda create -n teaching python=3.12
conda activate teaching
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. To open Jupyter notebooks:

```bash
jupyter notebook
```

---

## Repository Structure

```
teaching/
├── 01_basics/               # Python fundamentals
│   ├── data_structures.py   # Lists, tuples, dicts, sets
│   ├── strings_and_loops.py # String operations, enumerate, dicts
│   └── loan_calculator.py   # Practical loop example: loan payoff finder
│
├── 02_oop/                  # Object-Oriented Programming
│   └── bank_account.py      # BankAccount class + SavingsAccount inheritance
│
├── 03_modules/              # Python module and package system
│   ├── utils/
│   │   ├── __init__.py      # Package init with re-exports
│   │   ├── math_utils.py    # PI constant, add(), multiply()
│   │   └── str_utils.py     # String utilities (in progress)
│   ├── master.py            # Demonstrates various import styles
│   └── script.py            # Wildcard import example
│
├── 04_pandas/               # Data analysis with Pandas
│   ├── main.py              # Basic DataFrame operations
│   └── data/
│       ├── employees.csv    # Sample dataset (27 employees)
│       └── output.csv       # Processed output with calculated columns
│
├── notebooks/               # Jupyter notebooks
│   └── pandas-example.ipynb # Full Pandas walkthrough (filter, groupby, sort, export)
│
├── misc/                    # Scratch / miscellaneous files
├── requirements.txt
└── .gitignore
```

---

## Sections

### 01 — Basics
Core Python building blocks: data structures (list, tuple, dict, set), string manipulation, loops, and `enumerate`. Also includes a practical loan payoff calculator to demonstrate loops and conditionals in a real-world context.

### 02 — Object-Oriented Programming
Introduces classes, constructors (`__init__`), instance methods, the `__str__` magic method, and inheritance via `super()`. The `BankAccount` / `SavingsAccount` example simulates deposits, withdrawals, and interest with timestamps.

### 03 — Modules and Packages
Explains the Python module system: how to structure a package with `__init__.py`, the difference between importing a package vs. a module vs. a function, wildcard imports, and the `if __name__ == "__main__"` guard.

### 04 — Pandas
Hands-on data analysis using a sample employee dataset. Covers reading CSVs, selecting columns, filtering rows, creating derived columns, groupby aggregations, sorting, and exporting results.

### Notebooks
Jupyter notebooks for interactive exploration. Currently includes the full Pandas walkthrough with live output.
