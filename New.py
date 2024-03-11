import pandas as pd 
import numpy as np

df=pd.read_csv("D:\Python_Project\Dataset\Salaries.csv",skipinitialspace = True,encoding='cp1252')

print(df.columns)
x=df['JobTitle'].nunique()
print(x)

x = df[df['EmployeeName']=='ALBERT PARDINI'] ['JobTitle']
print(x)

x = df['BasePay'].describe()
print(x) #for maximum