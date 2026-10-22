# Algorithm Analysis Course — Midterm Assignment

## Project Structure
```text
AlgorithmAnalysis_Midterm/
├── README.md              # This file
├── REPORT.md              # Detailed project report
└── src/
    ├── insertion_sort.py  # Insertion Sort implementation
    └── bubble_sort.py     # Bubble Sort implementation
```

## Selected Algorithms
1. Insertion Sort — Builds the sorted array one item at a time, highly efficient for nearly sorted data.
2. Bubble Sort — Adjacent-swap sort with early-exit optimization.

## How to Build and Run

### Prerequisites
- Python 3.x installed on your system.

### Run
No compilation is needed for Python. Simply run the scripts directly from the terminal:

```bash
python src/insertion_sort.py
python src/bubble_sort.py
```

## Quick Complexity Summary

| Algorithm | Best | Average | Worst | Space | Stable |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |