import pandas as pd

"""data = {
    "Name_": ["Alice", "Bob", "Charlie", "Alice", "Bob"],
    "Department": ["IT", "HR", "IT", "HR", "IT"],
    "Salary": [5000, 4000, 6000, 5200, 4500],
    "Bonus": [500, 300, 600, 400, 450]
}
df = pd.DataFrame(data)
print(df)
print(df["Name_"])          # single column
print(df[["Name_", "Salary"]])  # multiple columns
# Employees from IT department
it_employees = df[df["Department"] == "IT"]
print(it_employees)
"""

df = pd.read_csv("employees.csv")
print(df)
# print(df.head())