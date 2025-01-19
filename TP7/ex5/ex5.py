import pandas as pd
path='TP7/ex5/employees.csv'
df=pd.read_csv(path)
print(f"the first 5 employees :{df.head()}")

if 'Salary' in df.columns:
    average_Salary=df['Salary'].mean()
    print(f"\nthe average salary is :{average_Salary}")
else:
    print("there is no salary column")
