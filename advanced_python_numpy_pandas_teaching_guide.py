"""
ADVANCED PYTHON: NUMPY AND PANDAS
Simplified step-by-step teaching notes, practical examples, exercises, and test.

Install first in the VS Code terminal:
    python -m pip install numpy pandas

NumPy is mainly for numerical arrays and calculations.
Pandas is mainly for organised data in tables.
This file is a teaching guide. The examples can be copied into separate files
and run section by section.
"""

# 1. LEARNING OBJECTIVES
"""
Students will learn to:
- Explain NumPy and Pandas.
- Create and calculate with NumPy arrays.
- Create Pandas Series and DataFrames.
- Select columns, filter rows, sort data, and calculate statistics.
- Read and write CSV files.
"""

# 2. WHAT IS NUMPY?
"""
NumPy means Numerical Python. It is useful for working with many numbers and
performing calculations on arrays.

Example: if scores contains [60, 70, 80], NumPy can add 5 to every score with
scores + 5, without writing a loop.
"""

# 3. WHAT IS PANDAS?
"""
Pandas helps us work with organised data, like a spreadsheet:
rows, columns, column names, and records.

Remember:
- NumPy: numerical arrays and calculations.
- Pandas: table-like data, filtering, sorting, and analysis.
"""

# 4. INSTALLING THE LIBRARIES
"""
Run this in the VS Code terminal, not as Python code:
    python -m pip install numpy pandas

If you use a virtual environment, activate it before installing.
"""

# 5. NUMPY: CREATE AN ARRAY
import numpy as np

scores = np.array([60, 70, 80, 90])

print("Scores:", scores)
print("First score:", scores[0])
print("Scores plus 5:", scores + 5)
print("Total:", np.sum(scores))
print("Average:", np.mean(scores))
print("Highest:", np.max(scores))
print("Lowest:", np.min(scores))

"""
Explanation:
- import numpy as np: imports NumPy using the short name np.
- np.array([...]): creates an array.
- scores[0]: gets the first item; Python indexes start at 0.
- scores + 5: adds 5 to every item.
- np.sum(): calculates the total.
- np.mean(): calculates the average.
- np.max() and np.min(): find the largest and smallest values.
"""

# 6. NUMPY: MORE CALCULATIONS
prices = np.array([100, 200, 300])

print("Prices:", prices)
print("Add 10:", prices + 10)
print("Double:", prices * 2)
print("Divide by 10:", prices / 10)

"""
NumPy performs each operation on every array element.
A normal Python list does not perform the same element-by-element arithmetic
when you write list + 5.
"""

# 7. PANDAS SERIES
import pandas as pd

score_series = pd.Series([60, 70, 80, 90])

print(score_series)
print("First value:", score_series.iloc[0])
print("Average:", score_series.mean())

"""
A Series is similar to one labelled column of data.
- pd.Series([...]) creates a Series.
- .iloc[0] selects the first item by position.
- .mean() calculates the average.
"""

# 8. PANDAS DATAFRAME
student_data = {
    "Name": ["Ada", "Bola", "Chidi", "Dayo"],
    "Age": [18, 20, 19, 21],
    "Score": [85, 72, 90, 66],
}

df = pd.DataFrame(student_data)
print(df)

"""
A DataFrame is like a spreadsheet table.
Each dictionary key becomes a column name.
Values at matching positions become the rows.
All column lists should have the same number of items.
"""

# 9. SELECTING COLUMNS AND ROWS
print("Names:")
print(df["Name"])

print("Scores:")
print(df["Score"])

print("First row:")
print(df.iloc[0])

print("First two rows:")
print(df.head(2))

"""
df["Name"] selects a column.
df.iloc[0] selects the first row by position.
df.head(2) displays the first two rows.
"""

# 10. FILTERING ROWS
high_scores = df[df["Score"] >= 80]
print("Students who scored 80 or above:")
print(high_scores)

adults = df[df["Age"] >= 20]
print("Students aged 20 or above:")
print(adults)

"""
Filtering keeps only rows where the condition is True.
For example, df["Score"] >= 80 checks every score, and df[condition] selects
the matching rows.
"""

# 11. SIMPLE DATA ANALYSIS
print("Total scores:", df["Score"].sum())
print("Average score:", df["Score"].mean())
print("Highest score:", df["Score"].max())
print("Lowest score:", df["Score"].min())
print("Number of records:", len(df))

"""
These methods can help analyse scores, sales, attendance, and survey results.
"""

# 12. SORTING DATA
ranked_df = df.sort_values("Score", ascending=False)
print("Highest score to lowest:")
print(ranked_df)

"""
sort_values("Score") sorts by the Score column.
ascending=False means highest to lowest.
ascending=True means lowest to highest.
"""

# 13. ADDING A COLUMN
df["Passed"] = df["Score"] >= 50
print(df)

"""
The Passed column will contain True when Score is 50 or above and False
otherwise.
"""

# 14. SAVE DATA TO A CSV FILE
df.to_csv("students.csv", index=False)

"""
CSV stands for Comma-Separated Values. It is a common spreadsheet data format.
to_csv() saves the DataFrame.
index=False stops Pandas from saving its row index as an extra column.
The file is saved in the current working directory unless a path is provided.
"""

# 15. READ DATA FROM A CSV FILE
loaded_df = pd.read_csv("students.csv")
print("Loaded from CSV:")
print(loaded_df)

"""
read_csv() loads a CSV file into a DataFrame.
If FileNotFoundError appears, check the filename and working directory.
"""

# 16. NUMPY AND PANDAS TOGETHER
"""
NumPy example:
    values = np.array([85, 72, 90])
    print(np.mean(values))

Pandas example:
    table = pd.DataFrame({"Score": [85, 72, 90]})
    print(table["Score"].mean())

Both libraries can be used in the same project.
"""

# 17. PRACTICAL CLASSROOM TASK
"""
TASK: STUDENT SCORE ANALYSER

Create a table with at least five students and their scores.
Your program must:
1. Display all students.
2. Display the average score.
3. Display the highest score.
4. Display students who scored at least 50.
5. Sort students from highest score to lowest.
6. Save the table as student_results.csv.
"""

class_results = {
    "Name": ["Ada", "Bola", "Chidi", "Dayo", "Efe"],
    "Score": [85, 45, 73, 92, 38],
}
results_df = pd.DataFrame(class_results)

print("All results:")
print(results_df)
print("Average:", results_df["Score"].mean())
print("Highest:", results_df["Score"].max())
print("Students who passed:")
print(results_df[results_df["Score"] >= 50])
print("Ranked results:")
print(results_df.sort_values("Score", ascending=False))
results_df.to_csv("student_results.csv", index=False)

# 18. COMMON ERRORS
"""
ModuleNotFoundError: No module named 'numpy' or 'pandas'
- Activate the correct virtual environment and install the libraries there.

FileNotFoundError while reading a CSV
- Check the filename and current working directory.

KeyError: 'Score'
- Check the exact column name and capitalisation. "Score" and "score" differ.

Useful checks:
    print(df.columns)
    print(df.head())
"""

# 19. LESSON SUMMARY
"""
- NumPy is mainly for numerical arrays and calculations.
- Pandas is mainly for organised data in tables.
- np.array() creates an array.
- pd.Series() creates a Series.
- pd.DataFrame() creates a DataFrame.
- df["Score"] selects a column.
- df[condition] filters rows.
- mean(), sum(), max(), and min() calculate statistics.
- sort_values() sorts rows.
- to_csv() saves data; read_csv() reads data.
"""

# 20. OBJECTIVE TEST — 15 QUESTIONS
"""
Choose ONE answer (A, B, C, or D) for each question. Each question is 1 mark.

1. What is NumPy mainly used for?
A. Website styling
B. Numerical calculations and arrays
C. Sending emails
D. Creating HTML pages

2. What is Pandas mainly used for?
A. Organised, table-like data
B. Playing audio
C. Drawing buttons
D. Opening network ports

3. Which command imports NumPy using the common alias np?
A. import numpy as np
B. import pandas as np
C. install numpy as np
D. from np import numpy

4. Which function creates a NumPy array?
A. pd.DataFrame()
B. np.array()
C. np.table()
D. pd.csv()

5. What does np.mean([10, 20, 30]) calculate?
A. Total
B. Largest number
C. Average
D. Smallest number

6. Which Pandas structure is like one labelled column?
A. Series
B. Socket
C. Function
D. Browser

7. Which Pandas structure represents a table with rows and columns?
A. Tuple
B. DataFrame
C. Integer
D. Boolean

8. What does df["Score"] select?
A. The Score column
B. Only the first row
C. The whole program
D. A CSV filename

9. What does df.head(2) display?
A. The last two rows
B. The first two rows
C. Two random columns
D. Rows with scores above 2

10. Which expression filters rows where Score is at least 50?
A. df["Score"] = 50
B. df("Score" >= 50)
C. df[df["Score"] >= 50]
D. df.head(50)

11. Which method calculates the average of a Pandas column?
A. mean()
B. average_now()
C. middle()
D. total()

12. Which method sorts rows using a chosen column?
A. sort_values()
B. arrange_rows()
C. order_file()
D. filter_values()

13. Which method saves a DataFrame as a CSV file?
A. read_csv()
B. to_csv()
C. save_python()
D. make_csv()

14. Which function reads a CSV file into a DataFrame?
A. pd.open_csv()
B. pd.read_csv()
C. np.read_table()
D. pd.load_python()

15. What should you do if Python reports "No module named pandas"?
A. Rename every Python file
B. Install Pandas in the Python environment being used
C. Delete the project
D. Change every variable to uppercase
"""

# 21. TEACHER'S ANSWER KEY
"""
Hide or remove this section before giving the test to students.

1. B
2. A
3. A
4. B
5. C
6. A
7. B
8. A
9. B
10. C
11. A
12. A
13. B
14. B
15. B
"""

if __name__ == "__main__":
    print("\nNUMPY AND PANDAS TEACHING GUIDE")
    print("Install the libraries with: python -m pip install numpy pandas")
