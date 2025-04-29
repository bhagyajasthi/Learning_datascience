# pandas Assignment: Getting Started with pandas

## Overview

This assignment will assess your understanding of core pandas concepts including Series, DataFrames, indexing, selection, arithmetic operations, and statistical summaries. It is based on Chapter 5 of *Python for Data Analysis* by Wes McKinney.

## Instructions

- Use only `pandas` and `numpy` (no external libraries).
- Submit a Jupyter notebook or `.py` file with your solutions.
- Include comments to explain your logic and output validation.

---

## Dataset

If no dataset is specified, create mock data manually using dictionaries, lists, or NumPy arrays as required.

---

## Task 1: Series and DataFrame Basics

1. **Series Creation**:
   - Create a Series containing five stock prices with custom index labels for company tickers (e.g., 'AAPL', 'GOOG', etc.).
   - Print its `index`, `values`, and `dtype`.

2. **DataFrame Creation**:
   - Construct a DataFrame using a dictionary of lists, with columns: 'Name', 'Department', 'Salary'.
   - Set custom row labels for employee IDs (e.g., 'EMP001', ...).

3. **Inspect the Data**:
   - Use `.head()`, `.tail()`, `.shape`, and `.dtypes` to inspect the DataFrame.

---

## Task 2: Reindexing and Dropping

1. Reindex the DataFrame to include an extra row index 'EMP999' and use forward fill (`ffill`) to populate it.

2. Drop:
   - The 'Department' column.
   - The row with employee ID 'EMP003'.

---

## Task 3: Selection and Filtering

1. Use `.loc[]` to select:
   - The 'Name' and 'Salary' for 'EMP002'.

2. Use `.iloc[]` to select:
   - The first 3 rows.

3. Filter the DataFrame to find:
   - Employees with salary above 60,000.
   - Employees in departments matching a list of ['IT', 'Finance'] using `isin()`.

---

## Task 4: Arithmetic and Alignment

1. Create a Series of bonuses indexed by employee IDs, with one ID missing and one extra.

2. Add the bonus Series to the 'Salary' column and observe alignment. Use `fill_value=0` to replace NaN with 0.

3. Calculate the percentage increase using broadcasting.

---

## Task 5: Function Application

1. Apply a lambda function to:
   - Convert all employee names to uppercase.

2. Use `.apply()` to:
   - Create a new column 'Net Salary' by applying a tax deduction of 10% to the 'Salary'.

---

## Task 6: Sorting and Ranking

1. Sort the DataFrame by:
   - Index (row labels).
   - Salary in descending order.

2. Add a 'Salary Rank' column using `.rank()` (use `method='min'` for tie breaking).

---

## Task 7: Duplicate Indexes

1. Create a Series with duplicate index labels.

2. Use `.loc[]` on the Series to retrieve all values for a duplicate index.

3. Comment on what happens when applying `.mean()` and `.sum()` on this Series.

---

## Task 8: Descriptive and Statistical Summary

1. Use `.describe()` on the numeric columns.

2. Calculate:
   - Mean, standard deviation, and cumulative sum of the 'Salary' column.
   - Index label with the maximum and minimum salary using `.idxmax()` / `.idxmin()`.

---

## Task 9: Correlation and Categorical Analysis

1. Create a new DataFrame with two numerical columns (e.g., 'Experience', 'Salary').

2. Compute:
   - Correlation and covariance matrix using `.corr()` and `.cov()`.

3. Use `.value_counts()` to:
   - Count the frequency of unique values in a categorical column (e.g., 'Department').

---

## Submission Guidelines

- Name your file as `pandas_assignment_<your_name>.ipynb` or `.py`.
- Ensure your code is well-formatted and tested.
- Submit it through the class LMS or email as instructed.

---

**Happy analyzing with pandas!**
