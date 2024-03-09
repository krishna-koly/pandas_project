import pandas as pd

# creating dataframe for analysis by creating a dictionary with key and values.

dict1 = {
    'Name': ['Priyang', 'Aadhya', 'Krisha', 'Vedant', 'Parshv', 'Mittal', 'Archana'],
    'Marks': [98, 89, 99, 87, 90, 83, 99],
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Male', 'Female', 'Female']
}

df = pd.DataFrame(dict1)
print(df)


#problem 01: Show the first 3 rows of Dataset
print(df.head(3))

#02. show the last 3 rows of dataset
print(df.tail(3))

#03.Find shape of our dataset
print(df.shape)
print("Number of rows:", df.shape[0])
print("Number of columns:" ,df.shape [1])

#Alternative approach 
#-- DataFrame doesn't have a row attribute. Instead, you should use the index attribute to access the DataFrame's index
#For Rows
no_of_rows = len(df.index)
print("Number of columns:" ,no_of_rows)
#for columns
no_of_col = len(df.columns)
print("Number of columns:" ,no_of_col)

#04 Get information about our dataset like total number of rows , total number of columns, Data type for each colums and the memory requirments

print(df.info())

#05 Checking the null values in Dataset
print(df.isnull().sum(axis=0))
#axis = 0 shows the data as column wise and axis =1 shows the data as row wise. as there is no null value in our dataset that's y we are getting 0

#6 Get overall statistics about dataset
print(df.describe())

#by default describe method only works for numerical valus that'y we are getting only marks column values
#if we want to get others column value through out this describe function then above code will not work. check below code for this
print(df.describe(include='all'))
#7 Find unique values for Gender Column
print(df['Gender'].unique())

#8 Display the number of unique count for Gender Column
print(df['Gender'].nunique())
#This will show the number of unique count of gender as there are two types of gender in our dataset thats y its showing 2 only.

#9 Display count of unique values in Gender Column
print(df['Gender'].value_counts())

#10 Find Total number of students having marks between 90 and 100.use Between method
#with between method solution
print(sum(df['Marks'].between(90,100)))

#without between method solution
print(df[(df['Marks']>=90) & (df['Marks']<=100)])
#this upper code shows which students have marks more then 90
print(len(df[(df['Marks']>=90) & (df['Marks']<=100)]))

#this len function here defines how many students has marks more than 90 and below 100.

#11 Find Average Marks
print(df['Marks'].mean())

#12Apply Method

def marks(x):
    return x//2
z = df['Marks'].apply(marks)
df['Half Marks'] = z
print(df)
#here we are adding a new column half marks into dataframe 

#using lamda function
z = df['Marks'].apply(lambda x:x/2)
print(z)

#13 Map Function
y= df['Gender'].map({'Male':1,'Female':0})
df['Male_Female']= y
print(df)

#14drop the column
#print(df.drop('Male_Female', axis=1))
#for deleteing multiple column we have to put it in a list
print(df.drop(['Male_Female','Half Marks'],axis=1,inplace = True))
print(df)

#15 Print the name of columns
print(df.columns)

#16 Print the rows
print(df.index)

#16 Sort the Database as per marks column in decending order
t = df.sort_values(by='Marks',ascending=False)
print(t)
#for sorting in different colums we have to use list for that
k= df.sort_values(by=['Marks','Gender'],ascending=False)
print(k)

#18 Display Name and marks only for female

print(df[df['Gender'] == 'Female'] [['Name','Marks']])


#Alternative Solution
print(df[df['Gender'].isin(['Female'])] [['Name','Marks']])
 


