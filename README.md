# Task 5 - Data Analysis on CSV Files

## Objective
Analyze sales data using Python and Pandas.

## Tools Used
- Python
- Pandas
- Matplotlib
- Jupyter Notebook / VS Code

## Files in this Repository
- `sales_data.csv` → sample sales dataset
- `script.py` → Python script for analysis
- `task5_data_analysis.ipynb` → notebook version
- `charts/` → generated bar charts

## Steps Performed
1. Loaded CSV file using Pandas
2. Displayed first 5 rows of data
3. Checked dataset info and shape
4. Checked for missing values
5. Created a new column `Total_Sales`
6. Used `groupby()` to calculate:
   - Total sales by product
   - Total sales by region
7. Created bar charts for data visualization

## Output
Basic insights were generated from the sales dataset using Python.

## Interview Questions Answers

### 1. What is Pandas used for?
Pandas is a Python library used for data analysis, data cleaning, and handling structured data.

### 2. What is a DataFrame?
A DataFrame is a two-dimensional table-like data structure in Pandas with rows and columns.

### 3. How do you read a CSV file?
Using:
```python
pd.read_csv("sales_data.csv")
