import pandas as pd 
import numpy as np

df=pd.read_csv("D:\Python_Project\Dataset\Salaries.csv",skipinitialspace = True,encoding='cp1252')
print(df.columns.tolist())

#01: Display Top 10 Rows of The Dataset

print(df.head(10))

#02: Check Last 10 Rows of The Dataset
print(df.tail(10))

#03: Find Shape of Our Dataset (Number of Rows And Number of Columns)
print(df.shape)

#shape is not a method of pandas it's an attribute of pandas. to check the shape of a dataset

#04: Getting Information About Our Dataset Like Total Number Rows, Total Number of Columns, Datatypes of Each Column And Memory Requirement
print(df.info())

#05.Check Null Values In The Dataset
x = df.isnull().sum()
print(x)

#06: Drop ID, Notes, Agency, and Status Columns

df = df.drop(['Id','Notes','Agency','Status'],axis=1)
print(df)


#07: Get Overall Statistics About The Dataframe

df = df.describe()
print(df)

#usually describe() function only works for numeric data. if we also want to see the categorized data then we should definately add include all inside the function.


#8:Find Occurrence of The Employee Names  (Top 5)

df = df['EmployeeName'].value_counts().head(10)
print(df)

#9: Find The Number of Unique Job Titles

x=df['JobTitle'].nunique()
print(x)

#10 Total Number of Job Titles Contain Captain
x = df[df['JobTitle'].str.contains('Captin',case=False)]
print(len(x))

#11  Display All the Employee Names From Fire Department
x = df[df['JobTitle'].str.contains('Fire',case=False)]['EmployeeName']
print(x)

#12 Find Minimum, Maximum, and Average BasePay
x = df['BasePay'].max()
print(x) #for maximum

x = df['BasePay'].min()
print(x) #for minimum

x = df['BasePay'].mean()
print(x) #for Average

# #13:  Replace 'Not Provided' in EmployeeName' Column to NaN 
df = df["EmployeeName"].replace(to_replace="Not provided",value="Nan")
print(df)

# #14: Drop The Rows Having 5 Missing Values
x = df.drop(df[df.isnull().sum(axis=1)==5].index,axis=0,inplace=True)
print(x)

# #15:  Find Job Title of ALBERT PARDINI
x = df[df['EmployeeName']=='ALBERT PARDINI'] ['JobTitle']
print(x)

# #16. How Much ALBERT PARDINI Make (Include Benefits)?

x = df[df['EmployeeName']=='ALBERT PARDINI'] ['TotalPayBenefits']
print(x)

# #17:.Display Name of The Person Having The Highest BasePay

x = df[df['BasePay'].max()==df['BasePay']]['EmployeeName']

#18: Find Average BasePay of All Employee Per Year 

x = df.groupby('Year').mean()['BasePay']
print(x)

#19 Find Average BasePay of All Employee Per JobTitle
x = df.groupby('JobTitle').mean()['BasePay']
print(x)

#20 Find Average BasePay of Employee Having Job Title ACCOUNTANT

x = df[df['JobTitle']=='ACCOUNTANT']['BasePay'].mean()
print(x)


#21 Find Top 5 Most Common Jobs

x = df['JobTitle'].value_counts().head(5)
print(x)





