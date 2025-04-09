# 🧩 Sudoku Solver Python
![Tests](https://github.com/Eleee28/sudoku-solver-python/actions/workflows/tests.yaml/badge.svg)

A simple Python Sudoku Solver that uses backtracking to fill in a 9x9 Sudoku puzzle. It takes a flat list of 81 integers as input (with `0` representing empty cells) and returns the solved board as a list of integers.

---

## 💡 Algorithm Overview

This project uses the **backtracking algorithm** to solve Sudoku puzzles. Backtracking is a recursive search approach commonly used in constraint satisfaction problems like Sudoku.

### Steps:

1. Search for an empty cell (represented as `0`)

2. Try placing digits `1-9` in that cell:

	- Check if the number is valid in the current **row**, **column** and **3x3 box**

3. If the number is valid:

	- Place it and continue recursively

4. If it leads to a dead end:

	- Backtrack (reset the cell and try another number)

5. Repeat until the entire board is filled or it's determined to be unsolvable

---

## ✅ Features

- Supports any standard 9x9 Sudoku board
- Detects unsolvable boards
- Validates input size
- Clean and modular design
- Tested with `unittest`

## 🧪 Running Tests

This project includes some unit tests to verify the correctness of the solver.

### Run tests locally:

~~~bash
python -m unittest discover -s . -p "test_sudoku.py"
~~~

Or simply:
~~~bash
python test_sudoku.py
~~~

## 🛠 Continuous Integration
GitHub Actions automatically runs the tests on every push or pull request.

## 📁 Project Structure
~~~
.
├── sudoku.py           # Sudoku solver logic
├── test_sudoku.py      # Unit tests
└── .github/
    └── workflows/
        └── tests.yaml   # GitHub Actions workflow
~~~

## 📌 Requirements
- Python 3.7+
- No external dependencies
