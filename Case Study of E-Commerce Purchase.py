import pandas as pd
df=pd.read_csv("D:\Python_Project\Dataset\Ecommerce Purchases")



#--------------------------------------------- Question and Solutions ----------------------------------------
#01 Display Top 10 Rows of The Dataset
print(df.head(10))

#02 Check Last 10 Rows of The Dataset
print(df.tail(10))

#03 Check Datatype of Each Column
print(df.columns.dtype)

#04 Check null values in the dataset
print(len(df[df.isnull()]))

#05 How many rows and columns are there in our Dataset?
print(len(df.columns)) # no_of_columns
print(len(df.index)) #no of rows

#06 Highest and Lowest Purchase Prices
print(df['Purchase Price'].max())  #maximum purchase price
print(df['Purchase Price'].min())  #minimum purchase price

#07 Find out the Average Purchase Price
print(df['Purchase Price'].mean())

#08 in this dataset how many people have French 'fr' as their Language?

x = df[df['Language'] == 'fr']
print(len(x))


#09 Find the Job Title  which Contains Engineer

z = df[df['Job'].str.contains('Engineer',case = False)]
print(len(z))

#10  Find The Email of the person with the following IP Address: 132.207.160.22
print(df.columns)
y = df[df['IP Address'] == '132.207.160.22'] ['Email']
print(y)

#11  How many People have Mastercard as their Credit Card Provider and made a purchase above 50

x = df[(df['CC Provider'] == 'Mastercard') & (df['Purchase Price']>50)]
print(len(x))

#12  Find the email of the person with the following Credit Card Number: 4664825258997302

z = df[df['Credit Card'] == 4664825258997302] ['Email']
print(z)

#13  How many people purchase during the AM and how many people purchase during PM?
print(df['AM or PM'].value_counts())

#14 How many people have a credit card that expires in 2020?
def check_expiry():
    count = 0
    for date in df['CC Exp Date']:
        if date.split('/') [1] == '20':
            count = count+1
    print(count)
print(check_expiry())

#Alternative Approach

z = df[df['CC Exp Date'].apply(lambda x:x[3:]=='20')]
print(len(z))

#15 What are the top 5 most popular email providers (e.g. gmail.com, yahoo.com, etc...)

z = df['Email'].apply(lambda x:x.split('@')[1]).value_counts().head()
print(z)
